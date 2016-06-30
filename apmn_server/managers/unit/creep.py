from .unit import Unit

class Creep(Unit):
    def __init__(self,name,max_hp,max_mp,damage,armor,pos_x,pos_y,unit_range):
        super().__init__(name,
                         max_hp,
                         max_mp,
                         damage,
                         armor,
                         True,
                         [""],
                         pos_x,
                         pos_y,
                         unit_range
                         )
    def move(self):
        pass

