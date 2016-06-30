

class Score:

    def __init__(self,unit, kill = 0,
            death = 0,
            assist = 0):
        self.unit = unit
        self.kill = kill
        self.death = death
        self.assist = assist

    def count_kill(self):
        self.kill = self.kill + 1

    def get_kill(self):
        return self.kill

    def count_dead(self):
        self.death = self.death + 1

    def get_dead(self):
        return self.death

    def count_assist(self):
        self.assist = self.assist + 1

    def get_assist(self):
        return self.assist

