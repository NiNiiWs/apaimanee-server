
import time
import threading
import json

class GameUnit:
    def __init__(self):
        self.damage = 0
        self.hp = 0
        self.armor = 0
        self.magic_resist = 0
        self.strenght = 0
        self.agility = 0

    def to_data_dict(self):
        result = dict(damage=self.damage,
                hp=self.hp,
                armor=self.armor,
                magic_resist=self.magic_resist,
                strenght=self.strenght,
                agility=self.agility)
        return result


class Player(GameUnit):
    def __init__(self, **kwargs):
        self.score_kills = 0
        self.score_deaths = 0
        self.score_assits = 0
        self.score_creep = 0
        self.position = [0, 0]
        self.name = "player"
        self.mana = kwargs.get('mana', 0)
        self.mage = kwargs.get('mage', 0)
        self.atk_speed = kwargs.get('atk_speed', 0)
        self.speed = kwargs.get('speed', 0)
        self.level = 1
        self.coin = 475
        self.hp_regen = kwargs.get('hp_regen', 0)
        self.mana_regen = kwargs.get('mana_regen', 0)
        self.time_death = 10


    def to_data_dict(self):
        result = dict(score_creep = self.score_creep,
                score_kills = self.score_kills,
                score_assits = self.score_assits,
                score_deaths = self.score_deaths,
                position = self.position,
                name = self.name,
                mana = self.mana,
                mage = self.mage,
                atk_speed = self.atk_speed,
                speed = self.speed,
                level = self.level,
                coin=self.coin,
                hp_regen=self.hp_regen,
                mana_regen=self.mana_regen,
                time_death=self.time_death
                )
        result.update(super().to_data_dict())
        return result


class Tower(GameUnit):
    def __init__(self):
        self.time_destroy = 0

    def to_data_dict(self):
        result = dict(time_destroy = self.time_destroy
                )
        result.update(super().to_data_dict())
        return result

class Creep(GameUnit):
    def __init__(self):
        self.position = [0, 0]

    def to_data_dict(self):
        result = dict(position = self.position)

        result.update(super().to_data_dict())
        return result

class Animal(GameUnit):
    def __init__(self, **kwargs):
        self.position = [0, 0]
        self.name = "name"
        self.hp_regen = kwargs.get('hp_regen', 0)
        self.time_deaths = 0

    def to_data_dict(self):
        result = dict(position = self.position,
                name = self.name,
                hp_regen = self.hp_regen,
                time_deaths  = self.time_deaths
                )

        result.update(super().to_data_dict())
        return result


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
            return

        game = self._room.rooms.get(game_msg['room_id'], None)
        if not game:
            print("no game room")
            return

        client_id = None
        for p in game.players:
            if p.token == game_msg.get('token', None):
                client_id = p.client_id

        if client_id is None:
            print("invalid token")
            return

        method = game_msg['method']

        if method == 'update_game_status':
            # update game status here
            for p in game.players:
                response = dict(game=game.to_data_dict(), method='synchronize_game_status')
                response_json = json.dumps(response)
                self.mqtt_client.publish(self.game_topic_synchonize(p.client_id, game_msg['room_id']), response_json)


    def game_topic_synchonize(self, client_id, room_id):
        return 'apaimanee/clients/{}/rooms/{}/synchronize'.format(client_id, room_id)

    def run(self):
        while self._running:
            time.sleep(self._sleep_time)

    def stop(self):
        self._running = False

