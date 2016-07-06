class Controller:
    '''
    The Controller class is abstract class for implement basic command to play
    MOBA game.
    '''
    pass
class HeroItem(Controller):
    '''
    Control hero about item.
    Example:
        1.Hero item using.
        2.Hero item selling.
        3.Hero item buying.
        4.Hero item checking type item.
    '''
    def buy_cheap_item(self,item_list):
        '''
            Control hero to buy item which cheapest in item_list and hero can
        buy. If hero can't buy it, this method will not buy and operate
        next Instruction.
        '''
        pass
    def buy_expensive_item(self,item_list):
        '''
           Control hero to buy item which most expensive in item_list and hero can
        buy. If hero can't buy it, this method will not buy and operate
        next Instruction.
        '''
        pass
    def buy_item_order(self,item_list):
        '''
           Control hero to buy respectively item which in item_list and hero can
        buy. If hero can't buy it, this method will not buy and operate
        next Instruction.
        '''
        pass
    def sell_item(self,item):
        '''
            Control hero to sell item which hero possess.
        '''
        pass
class Moving(Controller):
    '''
    Controlle hero about moving.
    Example:
        1.Hero move to required position.
        2.Hero move to the base.
        3.Hero stop moving.
    '''
    def move_hero(self,x,y):
        '''
        Control hero move to required position x and y.
        '''
        pass
    def move_to_base(self):
        '''
        Control hero move to own base.
        '''
        pass
    def stop_moving(self):
        '''
        Control hero stop moving.
        '''
        pass
class SkillUsing(Controller):
    '''
    Control hero about skill using.
    Example:
        1.hero using the skill which can use in the moment time.
        2.hero using the damaged skill.
        3.hero using the support skill.
        4.hero using the *escape skill.
        5.hero using order skill.
    *escape skill about change position the hero
    '''
    def use_skill(skill):
        pass
    def order_using__skill():
        pass
    def order_upgrade_skill():
        pass
class Attacking(Controller):
    '''
    Control hero about attacking.
    '''
    def SelectTarget(self,enemy):
        '''
        Control hero lock on target for attack.
        '''
        pass
    def SelectTargetLowHp(self):
        '''
        This method find enemy which have lowest Hp in enemy list to be the target.
        The enemy list is list of enemy which in the vision of hero.
        '''
        pass
    def SelectTargetHightHp(self):
        '''
        This method find enemy which have highest Hp in enemy list to be the target.
        The enemy list is list of enemy which in the vision of hero.
        '''
        pass
    def SelectNearTarget(self):
        '''
        This method find nearest enemy to be the target.
        '''
        pass


