
class GameUnit:
    def __init__(self):
        self.damage = 0
        self.hp = 0
        self.armor = 0
        self.magic_resist = 0
    def to_data_dict(self)
        result = dict(damage=self.damage,
                hp=self.hp)
        return result


class Player(GameUnit):
    def __init__(self, **kwargs):
        self.score_kills = 0
        self.score_deaths = 0
        self.score_assits = 0
        self.score_creep = 0
        self.position = [0, 0]
        self.name = "player"
        self.mana = kwargs.get('mana', 0)
        self.mage = kwargs.get('mage', 0)
        self.atk_speed = kwargs.get('atk_speed', 0)
        self.speed = kwargs.get('speed', 0)
        self.level = 1
        self.coin = 475
        self.hp_regen = kwargs.get('hp_regen', 0)
        self.mana_regen = kwargs.get('mana_regen', 0)
        self.time_death = 10

    def to_data_dict(self):
        result = dict(score_creep = self.score_creep,
                score_kills = self.score_kills,
                score_assits = self.score_assits,
                score_deaths = self.score_deaths,
                position = self.position,
                name = self.name,
                mana = self.mana,
                mage = self.mage,
                atk_speed = self.atk_speed,
                speed = self.speed,
                level = self.level,
                coin=self.coin,
                hp_regen=self.hp_regen,
                mana_regen=self.mana_regen,
                time_death=self.time_death
                )
        result.update(super().to_data_dict())
        return result


class Tower(GameUnit):
    def __init__(self):
        self.time_destroy = 0

    def to_data_dict(self):
        result = dict(time_destroy = self.time_destroy
                )
        result.update(super().to_data_dict())
        return result

class Creep(GameUnit):
    def __init__(self):
        self.position = [0, 0]

    def to_data_dict(self):
        result = dict(position = self.position)

        result.update(super().to_data_dict())
        return result

class Animal(GameUnit):
    def __init__(self, **kwargs):
        self.position = [0, 0]
        self.name = "name"
        self.hp_regen = kwargs.get('hp_regen', 0)
        self.time_deaths = 0

    def to_data_dict(self):
        result = dict(position = self.position,
                name = self.name,
                hp_regen = self.hp_regen,
                time_deaths  = self time_deaths
                )

        result.update(super().to_data_dict())
        return result


class GameStatusController:
    def __init__(self, mqtt_client):
        self.mqtt_client = mqtt_client



