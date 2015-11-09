from .base import Manager
from apmn_server import models

import datetime

class User(Manager):
    def login(self, payload):
        print('check login')
        email = payload.get('email')

        response = payload

        user = models.User.objects(email=email).first()

        if user:
            response['loggedin'] = True
            last_login = models.LastLogin(user=user)
            last_login.save()

            token = models.Token(user=user)
            token.accessed_date = datetime.datetime.now()
            token.expired_date = token.accessed_date + datetime.timedelta(days=1)
            token.save()
            token.reload()

            response['token'] = str(token.id)


        else:
            response['loggedin'] = False

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

