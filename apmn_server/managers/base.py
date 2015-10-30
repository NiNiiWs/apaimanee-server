
import json

class Manager:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

    def __get_rpc_topic(self, client_id):
        return 'apaimanee/clients/%s/response' % client_id

    def publish(self, topic, msg, qos=0, retain=False):
        msg_str = json.dumps(msg)
        if topic is not None:
            self.mqtt_client.publish(topic, msg_str, qos, retain)

    def rpc_response(self, msg, client_id):
        topic = self.__get_rpc_topic(client_id)
        self.publish(topic, msg, 1)

