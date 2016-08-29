from .unit import Unit
import math

class Creep(Unit):
    def __init__(self,data_unit,pos_x=0,pos_y = 0,unit_range = 10):
        super().__init__(data_unit,
                         True,
                         [""],
                         pos_x,
                         pos_y,
                         unit_range
                         )
        self.move_speed = data_unit.move_speed
        self.sensor ={}
        self.can_move = False

    def change_controller(self,id_controller):
        self.id_controller = id_controller

    def move(self,pos_x,pos_y):
        distance = math.sqrt(math.pow((self.pos_y-self.pos_y),2)+
                             math.pow((self.pos_x-pos_x),2)
                            )

        rad = (pos_y-self.pos_y)/(pos_x-self.pos_x)
        degree = math.atan(rad)
        force_x = self.move_speed * math.cos(degree)
        force_y = self.move_speed * math.sin(degree)
        force_x = force_x/30
        force_y = force_y/30
        if abs(self.pos_x)-pos_x < 0.001:
            self.pos_x += force_x
        if  abs(self.pos_y)-pos_y < 0.001:
            self.pos_y += force_y

    def attack(self):
        pass

    def to_data_dict(self):
        result = dict(id=self.id,
                name=self.name,
                max_hp=self.max_hp,
                current_hp=self.current_hp,
                hp_regen=self.hp_regen,
                max_mana=self.max_mana,
                current_mana=self.current_mana,
                mana_regen=self.mana_regen,
                damage=self.damage,
                armor=self.armor,
                take_damaged=self.take_damaged,
                buff_status=self.buff_status,
                pos_x=self.pos_x,
                pos_y=self.pos_y,
                range=self.range,
                id_controller=self.id_controller,
                alive=self.alive,
                move_speed=self.move_speed)
        return result
