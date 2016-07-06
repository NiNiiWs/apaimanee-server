
from apmn_server import models
import os
import json


class DataTower():
    def __init__(self, home_path):
        self.home_path = home_path
        self.tower_data_path = home_path + '/data/towers'

    def load(self):
        print(self.tower_data_path)
        print (os.listdir(self.tower_data_path))
        for filepath in os.listdir(self.tower_data_path):
            print (filepath)
            fp = open(self.tower_data_path+'/'+filepath, 'r')
            tower_dict = json.load(fp)
            print(tower_dict)
            tower = models.Tower.objects(name=tower_dict['name']).first()
            if tower:
                tower.update(**tower_dict)
            else:
                tower = models.Tower(**tower_dict)
            tower.save()
