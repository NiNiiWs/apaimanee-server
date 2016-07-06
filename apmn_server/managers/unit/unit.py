import uuid
from apmn_server import models
class Unit:
    def __init__(self,
                data_unit,
                take_damaged = False,
                buff_status = [""],
                position_x = 0,
                position_y = 0,
                unit_range = 20,
                id_controller = "system" #id_controller owner of unit for controll unit
                ):
        self.id = str(uuid.uuid4())
        self.data = None
        self.data_unit = data_unit
        self.name = self.data_unit.name
        self.max_hp = self.data_unit.hp
        self.current_hp = self.max_hp
        self.hp_regen = self.data_unit.hp_regen
        self.max_mana = self.data_unit.mana
        self.current_mana = self.max_mana
        self.mana_regen = self.data_unit.mana_regen
        self.damage = self.data_unit.damage
        self.armor = self.data_unit.armor

        self.take_damaged = take_damaged
        self.buff_status =buff_status
        self.pos_x = position_x
        self.pos_y = position_y
        self.range = unit_range
        self.id_controller = id_controller
        self.alive = True

    def get_current_hp(self):
        return self.current_hp

    def get_max_hp(self):
        return self.max_hp

    def get_max_mana(self):
        return self.max_mana

    def get_armor(self):
        return self.armor

    def get_take_damaged(self):
        return self.take_damaged

    def can_take_damaged(self):
        self.take_damaged = True

    def can_not_take_damaged(self):
        self.take_damaged = False

    def set_buff_status(self,buff):
        self.buff_status = buff

    def regend_hp(self, hp_regend = 0):
        self.current_hp += hp_regend

    def regend_mana(self, mana_regend = 0):
        regend_mana += mana_regend

    def reduce_hp(self,hp):
        if self.take_damaged:
            self.current_hp = self.current_hp - hp

    def reduce_mana(self,mana):
        if self.mana >= 0:
            self.mana = self.mana - mana

    def get_position(self):
        position = {"x":self.pos_x,"y":self.pos_y}
        return position
