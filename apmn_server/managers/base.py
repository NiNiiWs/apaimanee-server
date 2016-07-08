
import json
import datetime
from .. import models


from . import games
from . import battle_arena
from .unit import *
import bson

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.User):
            return dict(id=str(obj.id), username=obj.username)
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, games.ApaimaneeGame):
            return obj.to_data_dict()
        if isinstance(obj, games.Player):
            return obj.to_data_dict()
        if isinstance(obj, games.GameUnit):
            return obj.to_data_dict()
        if isinstance(obj, battle_arena.BattleArena):
            return obj.to_data_dict()
        if isinstance(obj, hero.Hero):
            return obj.to_data_dict()
        if isinstance(obj, tower.Tower):
            return obj.to_data_dict()
        if isinstance(obj, creep.Creep):
            return obj.to_data_dict()
        if isinstance(obj, bson.ObjectId):
            return str(obj)

        return json.JSONEncoder.default(self, obj)

class Manager:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

    def __get_rpc_topic(self, client_id):
        return 'apaimanee/clients/%s/response' % client_id

    def publish(self, topic, msg, qos=1, retain=False):
        msg_str = json.dumps(msg, cls=ComplexEncoder)
        if topic is not None:
            self.mqtt_client.publish(topic, msg_str, qos, retain)

    def rpc_response(self, msg, client_id):
        topic = self.__get_rpc_topic(client_id)
        self.publish(topic, msg, 1)

    def get_user(self, request):
        token_str = request.get('token')
        token = models.Token.objects(id=token_str).first()

        if token:
            return token.user

        # remove if release
        if token_str == 'test_token':
            return models.User.objects(username='test').first()

        return None

