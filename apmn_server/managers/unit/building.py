from .unit import Unit

class Building(Unit):
    def __init__(self,name,max_hp = 2000,max_mana =0,pos_x,posy):
        super.__init__(name,
                       max_hp,
                       max_mana,
                       0,
                       armor,
                       False,
                       [""],
                       pos_x,
                       pos_y
                       )
