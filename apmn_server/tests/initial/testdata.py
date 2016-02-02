from apmn_server import models

from apmn_server.initial.heroes import DataHero
#from apmn_server.initial.items import DataItem
import os
import sys

class DataHeroTest():
    def __init__(self):

        settings = {
                    'mongodb.db_name':'apmn',
                    'mongodb.host': 'localhost'
                    }
        models.initial(settings)

    def test_load(self):
        d = None
        if len(sys.argv) == 1:
            d = DataHero('.')
        else:
            d = DataHero(sys.argv[1])

        d.load()

if __name__ == '__main__':
    data_hero_test = DataHeroTest()
    data_hero_test.test_load()
