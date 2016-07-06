from apmn_server.mangers.base import Manager
class HeroController(Manager):
    '''
    The HeroController class is controlling the actor in serveral events.
    '''
    def __init__(self,hero_obj,mqtt_client):
        self.hero_obj = hero_obj
        '''
        Hero_obj is Object in class the game.
        '''

    def attack(self, Enemy):
        '''
        The attack method is controlling the actor to attack Enemy.
        '''
        pass

    def use_skill(self, target, hero_skill = 0):
        '''
        The use_skill method is controlling the actor use skill which actor
        have to target.
        '''
        pass

    def is_enemy(self,unit):
        '''
        The is_enemy method use to check Enemy of this actor.
        '''
        return type(unit) is Enemy

    def is_allies(self,unit):
        '''
            the is_allies method use to check allies of this actor.
        '''
        pass

    def move(self):
        '''
        The movement method move the actor.
        '''
        pass

class UsingItem:
    '''
    The UsingItem class
    '''
    def __init__(self,item):
        '''
        '''
        pass
    def can_use(self):
        '''
        The can_use method return true if the item can use in the time.
        '''
        pass
    def get_delay(self):
        '''
        The get_delay method return the delay of available the item.
        '''
        pass
    def get_stack_in_hero(self,hero):
        '''
        The get_stack method return the number of item in the hero.
        '''
        pass
    def get_prize_when_buy(self):
        '''
        The get_prize_when_buy method return prize of item in the shop.
        '''
        pass
    def get_prize_when_sell(self):
        '''
        The get_prize_when_sell method return prize of item when sell item.
        '''
        pass
    def get_damage(self):
        '''
        The get_damage method return damage of the item can make.
        '''
        pass

    def get_use_mana(self):
        '''
        The get_use_mana method return mana of item using.
        '''
        pass

    def can_buy_item(self,item):
        '''
        This method return boolean from item which can buy.
        '''
        pass

    def can_sell_item(self,item):
        '''
        This method return boolean from item which can sell.
        '''
        pass
    def get_own_item(self):
        '''
        This method return List of owner this item.
        '''
        pass

    def buy_item(self,item):
        '''
        This method control hero to buy item.
        '''
        pass

    def sell_item(self,item):
        '''
        This method control hero to sell item.
        '''
        pass


class HeroStatus:
    '''
    The HeroStatus class is monitor for look status or return status of hero
    object in the game.
    '''
    def __init__(self,hero):
        '''
        Hero is Class in Hero class in the game.
        '''
        self.hero = hero
#    @property
    def get_hp(self):
        '''
        This method return hp attibute  in Hero class.
        '''
        return self.hero

#    @property
    def get_mp(self):
        '''
        This method return mp attibute in Hero class.
        '''
        return self.mp

    def get_item_in_hero(self,hero):
        '''
            The get_item_in_hero method return the list of item in the actor who want
        to know.
        '''
        pass
    def get_enemy_hp(self,enemy):
        '''
                The get_enemy_hp method return hp in enemy in enemy_list attibute
            of Hero class.
            if enemy is'nt in enemy_list will return 0.
        '''
        pass
