
import json
from .. import models


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.User):
            return dict(id=str(obj.id), username=obj.username)
        return json.JSONEncoder.default(self, obj)

class Manager:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

    def __get_rpc_topic(self, client_id):
        return 'apaimanee/clients/%s/response' % client_id

    def publish(self, topic, msg, qos=0, retain=False):
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

        return None

