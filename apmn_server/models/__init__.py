import mongoengine as me
from .users import User, Token, LastLogin

def initial(setting):
        me.connect(setting.get('mongodb.db_name'), host=setting.get('mongodb.host'))
