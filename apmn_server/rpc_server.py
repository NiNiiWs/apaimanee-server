import json
import logging
logger = logging.getLogger(__name__)


class RPCServer:
    def __init__(self, controller, mqtt_client):
        self. rpc_methods = dict(
                login=controller.user.login,
                register=controller.user.register,
                create_room=controller.room.create_room,
                join_game=controller.room.join_game
                )
        self.controller = controller
        self.mqtt_client = mqtt_client

    def get_rpc_topic(self, client_id):
        return 'apaimanee/clients/%s/response' % client_id

    def get_payload(self, msg):
        return json.loads(msg.payload.decode('utf-8'))

    def publish(self, topic, msg, qos=0, retain=False):
        msg_str = json.dumps(msg)
        if topic is not None:
            self.mqtt_client.publish(topic, msg_str, qos, retain)

    def rpc_response(self, msg, client_id):
        topic = self.get_rpc_topic(client_id)
        self.publish(topic, msg, 1)

    def rpc_request(self, client, controller, msg):
        payload = self.get_payload(msg)

        print("rpc request :", payload)

        call_name=payload.get('method', None)
        if call_name is None:
            print('"%s" not found in register rpc callback',
                    payload.get('method', None))

        method = self.rpc_methods.get(call_name, None)
        print('get method', method)
        if method is not None:
            try:
                payload['responses'] = method(**payload['args'])
                payload['status'] = 'success'
            except Exception as e:
                logger.exception(e)
                payload['responses'] = None
                payload['status'] = 'error'
        else:
            payload['responses'] = None
            payload['status'] = 'fail'

        return self.rpc_response(payload, payload['client_id'])



