import paho.mqtt.client as mqttclient
import json
import uuid
import traceback
import sys
import os
import logging
import logging.config

from . import callbacks
from . import rpc_server
from . import controller
from . import models

logger = logging.getLogger('apmn')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
    client.subscribe("apaimanee/#")
    #client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode('utf-8'))
    pass

class ApaimaneeServer:
    def __init__(self, config_file=None):

        self.server_id = str(uuid.uuid1())
        self.mqtt_client = mqttclient.Client(self.server_id,
                clean_session=True)

        self.mqtt_client.on_connect = on_connect
        self.mqtt_client.on_message = on_message

        from .config import Configuration
        configuration = Configuration(config_file)
        self.settings = configuration.settings

        if not os.path.exists(self.settings['apmn.log_dir']):
            os.mkdir(self.settings['apmn.log_dir'])

        if config_file:
            logging.config.fileConfig(config_file)

        models.initial(self.settings)
        self.controller = controller.ApaimaneeController(self.mqtt_client)
        self.mqtt_client.user_data_set(self.controller)
        self.rpc_server = rpc_server.RPCServer(self.controller, self.mqtt_client)


    def reconnect(self):
        logger.info("apmn-server connect to mqtt server {} port {}".format(self.settings['mqtt.host'], self.settings['mqtt.port']))
        self.mqtt_client.connect(self.settings['mqtt.host'],
                self.settings['mqtt.port'],
                60)
        self.register_callback()

    def register_callback(self):
        self.mqtt_client.message_callback_add('apaimanee/clients/request', self.rpc_server.rpc_request)
        self.mqtt_client.message_callback_add('apaimanee/clients/+/rooms/+/update', self.controller.game_controller.on_game_message)
       #self.mqtt_client.message_callback_add('apaimanee/clients/+/rooms/api')
        self.mqtt_client.message_callback_add('apaimanee/hello', callbacks.hello)
        self.mqtt_client.message_callback_add('apaimanee/status', callbacks.status)

    def start(self):
        self.reconnect()
        try:
            self.mqtt_client.loop_forever()
        except Exception as e:
            logger.exception(e)
        finally:
            self.controller.stop()
            self.mqtt_client.disconnect()

if __name__ == '__main__':
    server = ApaimaneeServer()
    server.start()
