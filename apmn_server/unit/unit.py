import uuid
class Unit:
    def __init__(self,name= "",
                max_hp = 0,
                max_mana = 0,
                damage = 0,
                armor = 0,
                take_damaged = False,
                buff_status = [""],
                position_x = 0,
                position_y = 0,
                unit_range = 0
                ):
        self.id = str(uuid.uuid4())
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.max_mana = max_mana
        self.damage = damage
        self.armor = armor
        self.alive = True
        self.take_damaged = take_damaged
        self.pos_x = position_x
        self.pos_y = position_y
        self.range = unit_range

    def get_hp(self):
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

    def reduce__hp(self,hp):
        if self.take_damaged:
            self.current_hp = self.current_hp - hp

    def get_position(self):
        position = {"x":self.pos_x,"y":self.pos_y}
        return position
