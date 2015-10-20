import json

class ApaimaneeController:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client

    def login(self, payload):
        print('check login')
        username = payload.get('username')
        password = payload.get('password')

        response = payload
        response.pop('password')
        if password == 'password':
            response['loggedin'] = True


        self.mqtt_client.publish('apaimanee/clients/%s/response' % response['client_id'],
                json.dumps(response))

    def hello(self, payload):
        print('login first:', payload)

    def status(self, payload):
        print('controller status')
