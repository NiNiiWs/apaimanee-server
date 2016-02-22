
import time
import threading
import json
import datetime

from .managers.base import ComplexEncoder


class GameStatusController(threading.Thread):
    def __init__(self, mqtt_client, room):
        super().__init__()
        self.mqtt_client = mqtt_client
        self._room = room

        self._running = True
        self._sleep_time = 1

    def on_game_message(self, client, userdata, msg):
        game_msg = json.loads(msg.payload.decode('utf-8'))

        if not 'room_id' in game_msg:
            print('cannot find room_id')
            return

        game = self._room.rooms.get(game_msg['room_id'], None)
        if not game:
            print("no game room")
            return

        client_id = None
        player = None
        for p in game.players:
            if p.token == game_msg.get('token', None):
                client_id = p.client_id
                player = p

        if client_id is None:
            print("invalid token")
            return

        method = game_msg['method']
        args = game_msg['args']

        request = dict(game_msg=game_msg, args=args, player=player)
        response = dict()

        func = None
        try:
            func = getattr(game, method)
        except:
            print('can not find method:', method)
            return

        response = func(request)
        if response is None:
            return
        # response message
        if response.response_type == 'owner':
            self.response(response, client_id, game)
        if response.response_type == 'other':
            self.response_other(response, game, client_id)
        else:
            self.response_all(response, game)

    def response_other(self, response, game, client_id):
        for player in game.players:
            c_id = player.client_id
            if c_id == client_id:
                continue

            self.response(response, client_id, game)

    def response_all(self, response, game):
        for player in game.players:
            client_id = player.client_id
            self.response(response, client_id, game)

    def response(self, response, client_id, game):
        response.reponse_date = datetime.datetime.now()
        response_json = json.dumps(vars(response), cls=ComplexEncoder)
        self.mqtt_client.publish(self.game_topic_synchonize(client_id, game.room_id), response_json)

    def game_topic_synchonize(self, client_id, room_id):
        return 'apaimanee/clients/{}/rooms/{}/synchronize'.format(client_id, room_id)

    def run(self):
        while self._running:
            time.sleep(self._sleep_time)

    def stop(self):
        self._running = False

