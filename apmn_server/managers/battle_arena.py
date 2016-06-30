from .unit.hero import Hero
from .unit.building import Building
from .unit.creep import Creep
from apmn_server import models


class BattleArena:
    def __init__(self, players, size_x=1000, size_y=1000):
        self.players = players
        self.size = size_x
        self.size = size_y
        self.heros ={}

        self.unit_list = []

        self.team1 = []
        self.team2 = []

    def to_data_dict(self):
        return vars(self)

    def load_unit(self):
        for player in self.players:
            if player.team == "team1":
                self.team1.append(player)
            elif player.team == "team2":
                self.team2.append(player)


        #self.unit_list.append()
        print("load complete")
        pass
    def get_players_in_team(self,team):
        if team == "team1":
            print(self.team1)
        elif team =="team2":
            print(self.team2)
        else:
            print("this game has not this team:{0}".format(team))

    def get_players(self):
        return self.players

    def get_status_hero(self):
        pass

    def run(self):

        pass
