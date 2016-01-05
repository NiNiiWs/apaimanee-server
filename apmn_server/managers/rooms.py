from .base import Manager
from apmn_server import models
import uuid
import datetime

class Room(Manager):
    def __init__(self, mqtt_client):
        super().__init__(mqtt_client)
        self.rooms = dict()

    def create_room(self, request):
        room_name = request.get('room_name')
        response = dict()
        room_id = str(uuid.uuid4())
        user = self.get_user(request)
        response['room_id'] = room_id
        response['players'] = [user]
        self.rooms[room_id] = response

        return response

    def join_game(self, request):
        print("Join Game")
        room_id = request['args'].get('room_id', None)
        print(room_id)
        response = dict()
        room = self.rooms.get(room_id, None)

        if room:
            if len(room['players']) <= 10:
                user = self.get_user(request)
                if not user in room['players']:
                    room['players'].append(user)
                response['joined'] = True
            else:
                response['joined'] = False
        else:
            response['joined'] = False

        return response
