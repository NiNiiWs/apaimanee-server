from . import sensor
import math
class NearSenSor(SenSor):

    def __init__(self, unit, unit_list):
        super(self, unit,unit_list).__init__()

    def scan(self):
        unit_in_range = list()
        #u is unit
        for u in unit_list:
            dist_u = sqrt(pow((u.range.pos_x - self.unit.pos_x),2)+pow((u.range.pos_y-unit.range.pos_y),2))
            if dist_u <= self.unit.range:
                unit_in_range.append(u)
        pass



