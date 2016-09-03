from .building import Building
import math
from .sensor.sensor import Sensor
class Tower(Building):
    def __init__(self,data_tower):
        super().__init__(data_tower,
                         False,
                         [""],
                         data_unit.position_x,
                         data_unit.position_y)

        self.alive = True
        self.max_hp = self.data_tower.max_hp
        self.max_mana = 0
        self.current_hp = self.data_tower.current_hp
        self.mana = 0
        self.damage = self.data_tower.damage
        self.armor = self.data_tower.armor
        self.buff_status = self.data_tower.buff_status
        self.pos_x = self.data_tower.pos_x
        self.pos_y = self.data_tower.pos_y
        self.range = self.range
        self.id_controller = self.data_tower.id_controller

        

    def attack(self, enemy):
        pass

    def tower_collapse(self):
        self.alive = False

    def get_alive(self):
        self.alive = True

    def get_status(self):
        staus  = {
                "hp": self.current_hp,
                "alive": self.alve}


    def to_data_dict(self):
        result = dict(id_controller=self.id_controller,
                      name=self.name,
                      hp=self.hp,
                      current_hp=self.current_hp,
                      mana=self.mana,
                      damage=self.damage,
                      armor=self.armor,
                      buff_status=self.buff_status,
                      alive=self.alive
                      )


        return result
