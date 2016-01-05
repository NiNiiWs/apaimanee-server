from .base import Manager
from apmn_server import models
import uuid
import datetime

class Room(Manager):
    def __init__(self, mqtt_client):
        super().__init__(mqtt_client)
        self.rooms = dict()

    def create_room(self, name_room):
        response = dict()
        room_id = str(uuid.uuid4())
        user_id = payload.get['user_id']
        response['room_id'] = room_id
        print(room_id)
        response['players'] = [payload['user_id']]
        self.rooms['room_id'] = response

        return self.rpc_response(response, payload['client_id'])

    def join_game(self, payload):
        response = payload
        room_id = payload.get('room_id', None)

        room = self.rooms.get(room_id, None)
        print(room_id)
        response = payload
        if room:
            if len(response['players']) <= 10:
                response['players'].append(payload['user_id'])
                response['joined'] = True
            else:
                response['joined'] = False
        else:
            response['joined'] = False

        return self.rpc_response(response, payload['client_id'])
