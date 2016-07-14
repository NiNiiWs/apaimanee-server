import json

from . import managers
from . import game_controller

class ApaimaneeController:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client
        #self.api = managers.api_game
        self.user = managers.User(self.mqtt_client)
        self.room = managers.Room(self.mqtt_client)

        self.game_controller = game_controller.GameStatusController(self.mqtt_client, self.room)
        self.game_controller.start()

        # comment if release
        from .managers.rooms import ApaimaneeGame, Player, GameUnit
        from apmn_server import models
        test_room_id = 'test_room_id'
        u = models.User.objects(username='test').first()
        game = ApaimaneeGame(test_room_id, 'test_room_name', u)
        game.players.append(Player('test_client_id', u, 'test_token'))
        self.room.rooms[test_room_id] = game
        hero = models.Hero.objects(name='Sinsamut').first()
        game.game_space.heros[str(u.id)] = GameUnit(**dict(hero.to_mongo()))
        game.game_space.create_creep()
        game.start()
#        game.game_space.load_unit()
        #game.game_space.get_players_in_team("team1")


    def stop(self):
        self.game_controller.stop()

    def hello(self, payload):
        print('login first:', payload)

    def status(self, payload):
        self.user = game_controller()

    def create_room(self, payload):
        print('new_create_room', payload)

    def get_room(self):
        return self.room
