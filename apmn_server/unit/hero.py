#import sys
#import os

#PACKAGE_PARENT = '..'
#SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
#sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from unit import Unit

class Hero(Unit):
    def __init__(self,
                name,
                max_hp,
                max_mana,
                damage,
                status,
                armor = 0,
                magic_resis = 0,
                damage_speed = 0.5,
                move_speed = 330,
                position_x = 20,
                position_y = 20,
                ):
        super().__init__(name,
                         max_hp,
                         max_mana,
                         damage,
                         armor,
                         True,
                         [""],
                         position_x,
                         position_y
                         )
        self.level = 1
        self.current_exp = 0
        self.move_status = True
        self.status = status
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

    def move(self,x,y):
        if self.move_status:
            self.pos_x += (self.move_speed/100)
            self.pos_y += (self.move_speed/100)
        if self.pos_x < x+10 and self.pos_x > x-10 and self.pos_y < y+10 and self.pos_y > y-10:
            sefl.move_status = False
