import paho.mqtt.client as mqttclient
import json
import uuid

from . import callbacks
from . import controller

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
    client.subscribe("apaimanee/#")
    #client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode('utf-8'))
    print(msg.topic+" "+json.dumps(payload))

class ApaimaneeServer:
    def __init__(self):

        self.server_id = str(uuid.uuid1())
        self.mqtt_client = mqttclient.Client(self.server_id,
                clean_session=False)

        self.mqtt_client.on_connect = on_connect
        self.mqtt_client.on_message = on_message

        self.controller = controller.ApaimaneeController(self.mqtt_client)
        self.mqtt_client.user_data_set(self.controller)

    def reconnect(self):
        self.mqtt_client.connect("localhost", 1883, 60)
        self.register_callback()

    def register_callback(self):
        self.mqtt_client.message_callback_add('apaimanee/clients/request', callbacks.rpc_request)
        self.mqtt_client.message_callback_add('apaimanee/hello', callbacks.hello)
        self.mqtt_client.message_callback_add('apaimanee/status', callbacks.status)

    def start(self):
        self.reconnect()
        try:
            self.mqtt_client.loop_forever()
        except Exception as e:
            print(e)
        finally:
            self.mqtt_client.disconnect()

if __name__ == '__main__':
    server = ApaimaneeServer()
    server.start()