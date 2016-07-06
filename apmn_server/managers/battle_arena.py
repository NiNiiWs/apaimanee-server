from .unit.hero import Hero
#from .unit.building import Building
from .unit.creep import Creep
from apmn_server import models
from .scoreboard import ScoreBoard
from . import games
import json

class BattleArena:
    def __init__(self, players, size_x=1000, size_y=1000):
        self.players = players
        self.size = size_x
        self.size = size_y
        self.heros ={}
        self.unit_list = []

        self.hero_team1 = {}
        self.hero_team2 = {}
        self.creep_team1 = {}
        self.creep_team2 = {}
        self.nature_creep ={}
        self.scoreboard = ScoreBoard(self.hero_team1,self.hero_team2)

    def to_data_dict(self):
        battle_arena_data = dict(players = self.players,
                                 heros = self.heros,
                                 unit_list = self.unit_list
                            )
        return battle_arena_data

    def create_creep(self):
        c = models.Creep.objects(name = "Creep").first()
        c_data = games.GameUnit(**dict(c.to_mongo()))
        for i in range(4):
            creep = Creep(c_data)
            self.creep_team1[creep.id] = creep
       #pass

    def load_unit(self):
        for player in self.players:
            if player.team == "team1":
                self.hero_team1[player.id] = Hero(self.heros[player.id])

            elif player.team == "team2":
                self.hero_team2[player.id] = Hero(self.heros[player.id])
 #       self.scoreboard.update()

        #self.unit_list.append()
        print("load complete")

    def get_hero_team(self,team):
        if team == "team1":
            return self.hero_team1
        elif team =="team2":
           return self.hero_team2
        else:
           print("this game has not this team:{0}".format(team))

    def get_creep_team(self,team):
        if team == "team1":
            return self.creep_team1
        elif team =="team2":
           return self.creep_team2
        else:
           print("this game has not this team:{0}".format(team))

    def get_players(self):
        return self.players

    def run(self):
        for c in self.creep_team1:
            self.creep_team1[c].move(50,50)
        for c in self.creep_team1:
            print(str(self.creep_team1[c].pos_x) +" "+str(self.creep_team1[c].pos_y))
 
        pass
