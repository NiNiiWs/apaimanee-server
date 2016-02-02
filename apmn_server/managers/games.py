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

    def ready(self):
        response = dict(method='wait')
        return response

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


