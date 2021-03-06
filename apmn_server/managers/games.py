import uuid
import datetime
import time
import json
import threading

from .battle_arena import BattleArena

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
        self.id = str(user.id)
        self.user = user
        self.token = token
        self.ready = False
        self.team = 'team1'

    def to_data_dict(self):
        result = dict(id=self.id,
                username=self.user.username,
                ready=self.ready,
                team=self.team
                )
        return result

class GameResponse:
    def __init__(self, method, args=None, response_type='all', qos=0):
        self.response_type = response_type
        self.args = args
        self.method = method
        self.qos = qos

class ApaimaneeGame(threading.Thread):
    def __init__(self, room_id, room_name, owner,game_controller):
        super().__init__()
        self.status = 'wait'
        self.room_id = room_id
        self.room_name = room_name
        self.players = []
        self.game_space = BattleArena(self.players)#GameSpace()
        self.owner=owner
        self.ready_time = None
        self.game_controller = game_controller

    def run(self):
        while self.status != 'stop':
            if self.status == 'play':
                diff_time = datetime.datetime.now() - self.ready_time
                print(diff_time.seconds)
                if diff_time.seconds % 15 == 0 and diff_time.seconds > 0:
                    self.game_space.create_creep()
                    print('creat_creep')
                    self.game_controller.response_all(self.update_game(),self)
                for creep_id in self.game_space.creep_team1:
                    creep = self.game_space.creep_team1[creep_id]
                    creep.move(500,500)
                    print( "{0} {1} ".format(creep.pos_x,creep.pos_y))
            time.sleep(1)

    def update(self, request):
        print("update", request)

    def ready(self, request):
        player = request['player']
        player.ready = True
        player_ready_count = len([p for p in self.players if p.ready])
        print("ready count:", player_ready_count)
        self.status = 'play'
        self.ready_time = datetime.datetime.now()
        if player_ready_count != len(self.players):
            return

        response = GameResponse(method='start_game', qos=1)
        return response

    def update_game(self):
        args = dict(game_space=self.game_space)
        response = GameResponse(method='update_game',
                args= args,
                response_type='owner',
                qos=1)
        return response

    def initial(self, request):
        player = request['player']
        self.game_space.load_unit()
        args = dict(players=self.players, player=player, game_space=self.game_space)
        response = GameResponse(method='initial_game',
                args=args,
                response_type='owner',
                qos=1)
        return response

    def move_hero(self, request):

        params = request['args']
        x = params['x']
        y = params['y']
        player = request['player']
        hero = self.game_space.heros[player.id]
        hero.target = dict(x=x, y=y)
        args = dict(x=x, y=y, player_id=player.id)
        response = GameResponse(method='move_hero',
                args=args,
                response_type='other')

        return response

    def skill_action(self, request):
        params = request['args']
        skill = params['skill']
        player = request['player']

        args = dict(skill=skill, player_id=player.id)
        response = GameResponse(method='skill_action',
                args=args,
                response_type='other')

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


