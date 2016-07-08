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
                alive=self.alive,)
        return result
