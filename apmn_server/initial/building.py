
from apmn_server import models
import os
import json

class DataBuilding():
    def __init__(self, home_path):
        self.home_path = home_path
        self.building_data_path = home_path + '/data/buildings'
    def load(self):
        print(self.building_data_path)
        print (os.listdir(self.building_data_path))
        for filepath in os.listdir(self.building_data_path):
            print (filepath)
            fp = open(self.hero_data_path+'/'+filepath, 'r')
            building_dict = json.load(fp)
            print(_dict)
            tower = models.Tower.objects(name=building_dict['name']).first()
            if hero:
                building.update(**building_dict)
            else:
                building = models.Building(**building_dict)
            building.save()
