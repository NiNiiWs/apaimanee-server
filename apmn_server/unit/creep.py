from .unit import Unit

class Creep(unit):
    def __init__(self,name="creep",max_hp,max_mp,armor,pos_x,pos_y):
        super().__init__(name,
                         max_hp,
                         max_mp,
                         armor,
                         True,
                         [""],
                         pos_x,
                         pos_y)

    def

