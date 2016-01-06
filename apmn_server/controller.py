import json

from . import managers
from . import game_controller


class ApaimaneeController:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

        self.user = managers.User(self.mqtt_client)
        self.room = managers.Room(self.mqtt_client)

        self.game_controller = game_controller.GameStatusController(self.mqtt_client, self.room)
        self.game_controller.start()

    def stop(self):
        self.game_controller.stop()

    def hello(self, payload):
        print('login first:', payload)

    def status(self, payload):
        self.user = game_controller()

    def create_room(self, payload):
        print('new_create_room', payload)
