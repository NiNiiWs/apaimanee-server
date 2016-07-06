from .building import Building

class Tower(Building):
    def __init__(self,data_tower):
        super().__init__(data_tower)

    def attack(self,enemy):
        pass

