from .base import Manager
from apmn_server import models
import uuid
import datetime
import json


class Player:
    def __init__(self, client_id, user, token):
        self.client_id = client_id
        self.user = user
        self.token = token

class ApaimaneeGame:
    def __init__(self, room_id, room_name):
        self.status = 'wait'
        self.room_id = room_id
        self.room_name = room_name
        self.players = []
        self.game_object = None

    def to_data_dict(self):
        result = dict(status=self.status,
                room_id=self.room_id,
                players=[str(p.user.id) for p in self.players],
                game_object=self.game_object
                )
        return result

    def to_json(self):
        result = self.to_data_dict()
        result_json = json.dumps(result)
        return result_json


class Room(Manager):
    def __init__(self, mqtt_client):
        super().__init__(mqtt_client)
        self.rooms = dict()

    def create_room(self, request):
        room_name = request.get('room_name')
        room_id = str(uuid.uuid4())

        user = self.get_user(request)

        game_status = ApaimaneeGame(room_id, room_name)
        game_status.players.append(Player(request['client_id'], user, request['token']))

        self.rooms[room_id] = game_status

        return game_status.to_data_dict()

    def join_game(self, request):
        print("Join Game")
        room_id = request['args'].get('room_id', None)
        print(room_id)
        response = dict()
        game = self.rooms.get(room_id, None)

        if game_status:
            if len(game.players) <= 10:
                user = self.get_user(request)
                for p in game.players:
                    if user != game.user:
                        game.players.append(Player(request['client_id'], user, request['token']))
                        response['joined'] = True
                        response['room_id'] = room_id
            else:
                response['joined'] = False
        else:
            response['joined'] = False

        return respons

    def start_game(self, request):
        room_id = request['args'].get('room_id', None)
        game = self.rooms.get(room_id, None)
        game.status = 'play'

        return dict(status='play')

