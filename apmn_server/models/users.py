import mongoengine as me
import datetime
import hashlib


class User(me.Document):
    meta = {'collection': 'users'}

    username = me.StringField(required=True)
    password = me.StringField(required=True)
    email = me.EmailField(required=True, unique=True)
    first_name = me.StringField(max_length=100, required=True)
    last_name = me.StringField(max_length=100)

    status = me.StringField(max_length=100, required=True, default="active")
#   roles = me.ListField(me.ReferenceField('Role'))

    registration_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    updated_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)

    ip_address = me.StringField(
        max_length=100, required=True, default='0.0.0.0')

    def hash_password(password):
        m = hashlib.sha512()
        m.update(password.encode('utf-8'))
        return m.hexdigest()

    def set_password(self, password):
        self.password = User.hash_password(password)

    def check_password(self, password):
        return hash_password(password) == self.password


# class Role(me.Document):
    # meta = {'collection': 'roles'}

    # name = me.StringField(max_length=100, required=True)

    # created_date = me.DateTimeField(
        # required=True, default=datetime.datetime.now)
    # updated_date = me.DateTimeField(
        # required=True, default=datetime.datetime.now)

    # ip_address = me.StringField(
        # max_length=100, required=True, default='0.0.0.0')


class Token(me.Document):
    meta = {'collection': 'tokens'}

    user = me.ReferenceField('User', dbref=True)
    accessed_date = me.DateTimeField(required=True)
    expired_date = me.DateTimeField(required=True)
    ip_address = me.StringField(
        max_length=100, required=True, default='0.0.0.0')

class LastLogin(me.Document):
    meta = {'collection': 'lastlogin'}

    user = me.ReferenceField('User', dbref=True)
    loggedin_date = me.DateTimeField(
        required=True, default=datetime.datetime.now)
    client_id = me.StringField()

