from apmn_server import models

from apmn_server.initial.heroes import DataHero
from apmn_server.initial.items import DataItem
import os

class DataHeroTest():
    def __init__(self):

        settings = {
                    'mongodb.db_name':'apmn',
                    'mongodb.host': 'localhost'
                    }
        models.initial(settings)

    def test_load(self):
        d = DataHero('/home/aran/projects/apaimanee-server')
        d.load()

if __name__ == '__main__':
    data_hero_test = DataHeroTest()
    data_hero_test.test_load()
