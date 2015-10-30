import json

from . import managers


class ApaimaneeController:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

        self.user = managers.User(self.mqtt_client)



    def hello(self, payload):
        print('login first:', payload)

    def status(self, payload):
        print('controller status')

    def create_room(self, payload):
        print('new_create_room', payload)
