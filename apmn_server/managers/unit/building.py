from .unit import Unit

class Building(Unit):
    def __init__(self,data_unit):
        super().__init__(data_unit,
                       False,
                       [""],
                       data_unit.position_x,
                       data_unit.position_y
                       )
    def toggle_take_damaged(self):
        self.take_damaged = not self.take_damaged
