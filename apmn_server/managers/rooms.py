from .base import Manager
from apmn_server import models
import uuid
import datetime

class Room(Manager):
    def __init__(self, mqtt_client):
        super().__init__(mqtt_client)
        self.rooms = dict()

    def create_room(self, payload):
        response = payload
        room_id = str(uuid.uuid4())
        response['room_id'] = room_id
        self.rooms[room_id] = response

        return self.rpc_response(response, payload['client_id'])


