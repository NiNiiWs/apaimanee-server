from .base import Manager

from apmn_server import models

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

    def register(self, payload):
        print('check register')
        username = payload.get('username')
        password = payload.get('password')
        email = payload.get('email')
        first_name = payload.get('first_name')
        last_name = payload.get('last_name')
        user = models.User(username=username,email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        user.reload()


        response = payload
        if hasattr(user, 'id'):
            response['id'] = user.id
            response['registed'] = True
        else:
            response['registed'] = False

        return self.rpc_response(response, payload.get('client_id'))

