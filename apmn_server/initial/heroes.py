
from apmn_server import models
import os
import json


class DataHero():
    def __init__(self, home_path):
        self.home_path = home_path
        self.hero_data_path = home_path + '/data/heroes'

    def load(self):
        print(self.hero_data_path)
        print (os.listdir(self.hero_data_path))
        for filepath in os.listdir(self.hero_data_path):
            print (filepath)
            fp = open(self.hero_data_path+'/'+filepath, 'r')
            hero_dict = json.load(fp)
            print(hero_dict)
            hero = models.Hero.objects(name=hero_dict['name']).first()
            if hero:
                hero.update(**hero_dict)
            else:
                hero = models.Hero(**hero_dict)
            hero.save()
