from .unit import Unit

class Building(Unit):
    def __init__(self,data_unit,pos_x,pos_y):
        super.__init__(data_unit,
                       False,
                       [""],
                       pos_x,
                       pos_y
                       )
    def toggle_take_damaged(self):
        self.take_damaged = not self.take_damaged
