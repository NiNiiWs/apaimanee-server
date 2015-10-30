from .base import Manager

class User(Manager):
    def login(self, payload):
        print('check login')
        username = payload.get('username')
        password = payload.get('password')

        response = payload
        response.pop('password')
        if password == 'password':
            response['loggedin'] = True

        return self.rpc_response(response, payload.get('client_id'))



