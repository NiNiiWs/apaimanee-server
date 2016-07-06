import mongoengine as me
import hashlib
import datetime


class HeroSkill(me.EmbeddedDocument):

    describtion = me.StringField(max_length=2000, required=True)
    name = me.StringField(required=True)
    damage = me.ListField(me.IntField())
    magic = me.ListField(me.IntField())
    used_mana = me.ListField(me.IntField())
    cooldown = me.ListField(me.IntField())
    buffs_damage = me.ListField(me.IntField())
    reduced_damage = me.ListField(me.IntField())
    buffs_armor =  me.ListField(me.IntField())
    reduced_armor = me.ListField(me.IntField())
    buffs_mana = me.ListField(me.IntField())
    buffs_hp = me.ListField(me.IntField())
    reduce_hp = me.ListField(me.IntField())
    buffs_strength = me.ListField(me.IntField())
    buffs_agi =  me.ListField(me.IntField())
    sight_range = me.ListField(me.IntField())
    attack_range =  me.ListField(me.IntField())
    attack_speed =  me.ListField(me.IntField())
    stun_duration = me.ListField(me.IntField())
    radius = me.ListField(me.IntField())
    cast_delay = me.ListField(me.IntField())
    duration = me.ListField(me.IntField())

class Hero(me.Document):
    meta = {'collection': 'heroes'}

    describtion = me.StringField(max_length=2000, required=True)
    name = me.StringField(max_length=100, required=True, unique=True)
    hp = me.IntField(required=True)
    mana = me.IntField(required=True)
    hp_regen = me.FloatField(required=True)
    mana_regen = me.FloatField(required=True)
    strength = me.IntField(required=True)
    agility = me.IntField(required=True)
    damage = me.IntField(required=True)
    damage_critical = me.FloatField(required=True)
    magic = me.IntField(required=True)
    armor = me.IntField(required=True)
    magic_resis = me.IntField(required=True)
    damage_speed = me.FloatField(required=True)
    move_speed = me.IntField(required=True)
    skills = me.ListField(me.EmbeddedDocumentField(HeroSkill))


class Creep(me.Document):
    meta = {'collection': 'creeps'}

    name = me.StringField(max_length=500, required=True)
    damage = me.IntField(required=True)
    magic = me.IntField(required=True)
    hp = me.IntField(required=True)
    hp_regen = me.FloatField(required=True)
    mana = me.IntField(required=True)
    mana_regen = me.FloatField(required=True)
    armor = me.IntField(required=True)
    magic_resis = me.IntField(required=True)
    move_speed = me.IntField(required=True)
    damage_speed = me.IntField(required=True)
    money = me.IntField(required=True)
    position_x = me.IntField(required=True)
    position_y = me.IntField(required=True)

class Tower(me.Document):
    meta = {'collection': 'towers'}

    name = me.StringField(max_length=100, required=True)
    hp = me.IntField(required=True)
    mana = me.IntField(required=True)
    hp_regen = me.IntField(required=True)
    mana_regen = me.IntField(required=True)
    damage = me.IntField(required=True)
    armor = me.IntField(required=True)
    damage_speed = me.IntField(required=True)
    magic_resis = me.IntField(required=True)
    damage_range = me.FloatField(required=True)
    cost = me.IntField(required=True)
    position_x = me.IntField(required=True)
    position_y = me.IntField(required=True)

class Item(me.Document):
    meta = {'collection': 'items'}

    name = me.StringField(max_length=100, required=True)
    describtion = me.StringField(max_length=500, required=True)
    damage = me.IntField(required=True)
    magic = me.IntField(required=True)
    hp = me.IntField(required=True)
    hp_regen = me.IntField(required=True)
    mana = me.IntField(required=True)
    mana_regen = me.IntField(required=True)
    cooldown_skills_reduce = me.IntField(required=True)
    buffs_armor = me.IntField(required=True)
    buffs_magic = me.IntField(required=True)
    damage_speed = me.IntField(required=True)
    move_speed = me.IntField(required=True)
    cirtical_damage = me.FloatField(required=True)
    cost = me.IntField(required=True)



