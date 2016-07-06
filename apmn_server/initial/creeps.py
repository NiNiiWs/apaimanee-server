
from apmn_server import models
import os
import json


class DataCreep():
    def __init__(self, home_path):
        self.home_path = home_path
        self.creep_data_path = home_path + '/data/creeps'
        self.dir = os.listdir( home_path )

    def load(self):
        for f in self.dir:
            print(f)
        print(self.creep_data_path)
        print (os.listdir(self.creep_data_path))
        for filepath in os.listdir(self.creep_data_path):
            print (filepath)
            fp = open(self.creep_data_path+'/'+filepath, 'r')
            creep_dict = json.load(fp)
            print(creep_dict)
            creep = models.Creep.objects(name=creep_dict['name']).first()
            if creep:
                creep.update(**creep_dict)
            else:
                creep = models.Creep(**creep_dict)
            creep.save()
