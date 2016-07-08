#import sys
#import os

#PACKAGE_PARENT = '..'
#SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
#sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from .unit import Unit

class Hero(Unit):
    def __init__(self,
                data_unit,
                position_x = 20,
                position_y = 20,
                unit_range = 50, #self.range = unit_range
                id_controller = 'system'
                ):
        super().__init__(
                         data_unit,
                         True,
                         [""],
                         position_x,
                         position_y,
                         unit_range,
                         id_controller
                         )
        self.str = self.data_unit.strength
        self.agi = self.data_unit.agility
        self.damage_critical = self.data_unit.damage_critical
        self.magic = self.data_unit.magic
        self.magic_resis = self.data_unit.magic_resis
        self.damage_speed = self.data_unit.damage_speed
        self.move_speed = self.data_unit.move_speed
        self.skills = self.data_unit.skills
        self.level = 1
        self.kill = 0
        self.death = 0
        self.assist = 0
        self.lasthit = 0
        self.current_exp = 0
        self.move_status = True
        self.act_status = ""
        self.time_to_born = 0

    def level_up(self):
        if self.level <=25:
            self.level = self.level + 1

    def die(self):
        self.alive = False
        self.time_to_born = self.level*15;

    def countdown_to_born(self):
        if self.time_to_born > 0:
            self.time_to_bone -=1

    def reborn(self):
        if not self.alive:
            self.countdown_to_born()
            if self.time_to_born ==0:
                self.alive = True
                self.current_hp = self.max_hp

    def get_alvie(self):
        self.alive = True

    def get_status(self):
        status = {
                "hp": self.current_hp,
                "mana": self.current_mana,
                "str": self.str,
                "agi": self.agi,
                "damage": self.damage_critical,
                "magic": self.magic,
                "magic_resis": self.magic_resis,
                "damage_speed": self.damage_speed,
                "move_speed": self.move_speed,
                "skills": self.skills,
                "level": self.level,
                "kill": self.kill,
                "death": self.death,
                "assist": self.assist,
                "lasthit": self.lasthit,
                "current_exp":self.current_exp
                 }
        return status

    def move(self,x,y):
        if self.move_status:
            self.pos_x += (self.move_speed/100)
            self.pos_y += (self.move_speed/100)
        if self.pos_x < x+10 and self.pos_x > x-10 and self.pos_y < y+10 and self.pos_y > y-10:
            sefl.move_status = False

    def to_data_dict(self):
        result = dict(take_damaged=self.take_damaged,
                buff_status=self.buff_status,
                id_controller=self.id_controller,
                id=self.id,
                name=self.name,
                max_hp=self.max_hp,
                current_hp=self.current_hp,
                hp_regen=self.hp_regen,
                max_mana=self.max_mana,
                current_mana=self.current_mana,
                mana_regen=self.mana_regen,
                damage=self.damage,
                armor=self.armor,
                alive=self.alive,
                pos_x=self.pos_x,
                pos_y=self.pos_y,
                range=self.range,
                str=self.str,
                agi=self.agi,
                damage_critical=self.damage_critical,
                magic=self.magic,
                magic_resis=self.magic_resis,
                damage_speed=self.damage_speed,
                move_speed=self.move_speed,
                skills=self.skills,
                kill=self.skills,
                death=self.death,
                assist=self.assist,
                lasthit=self.lasthit,
                current_exp=self.current_exp,
                move_status=self.move_status,
                act_status=self.act_status,
                time_to_born=self.time_to_born)
        return result
