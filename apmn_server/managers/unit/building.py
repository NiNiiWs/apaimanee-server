from .unit import Unit

class Building(Unit):
    def __init__(self, name,max_hp,max_mana,armor,pos_x,pos_y):
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
