import uuid
import datetime
import json

class GameUnit:
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def to_data_dict(self):
        return vars(self)

class GameSpace:
    def __init__(self):
        self.heros = {}

    def to_data_dict(self):
        return vars(self)


class Player:
    def __init__(self, client_id, user, token):
        self.client_id = client_id
        self.user = user
        self.token = token
        self.ready = False
        self.team = 'team1'

    def to_data_dict(self):
        result = dict(id=str(self.user.id),
                username=self.user.username,
                ready=self.ready,
                team=self.team
                )
        return result

class GameResponse:
    def __init__(self, method, args=None, response_type='all'):
        self.response_type = response_type
        self.args = args
        self.method = method

class ApaimaneeGame:
    def __init__(self, room_id, room_name, owner):
        self.status = 'wait'
        self.room_id = room_id
        self.room_name = room_name
        self.players = []
        self.game_space = GameSpace()
        self.owner=owner

    def ready(self, request):
        player = request['player']
        player.ready = True

        player_ready_count = len([p for p in self.players if p.ready])
        if player_ready_count != len(self.players):
            return

        response = GameResponse(method='start_game')
        return response

    def initial(self, request):
        player = request['player']

        args = dict(players=self.players, player=player, game_space=self.game_space)
        response = GameResponse(method='initial_game',
                args=args,
                response_type='owner')
        return response


    def to_data_dict(self):
        result = dict(status=self.status,
                    room_id=self.room_id,
                    room_name=self.room_name,
                    owner=self.owner,
                    players=[str(p.user.id) for p in self.players if p.user],
                    game_space=self.game_space
                )
        return result

    def to_json(self):
        result = self.to_data_dict()
        result_json = json.dumps(result)
        return result_json


