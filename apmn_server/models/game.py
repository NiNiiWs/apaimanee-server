import mongoengine as me
import hashlib
import datetime


class HeroSkill(me.EmbeddedDocument):

    describtion = me.StringField(max_length=500, required=True)
    name = me.StringField(required=True)
    damage = me.IntField(required=True)
    magic = me.IntField(required=True)
    used_mana = me.IntField(required=True)
    cooldown = me.IntField(required=True)
    buffs_damage = me.IntField(required=True)
    reduced_damage = me.IntField(required=True)
    buffs_armor = me.IntField(required=True)
    reduced_armor = me.IntField(required=True)
    buffs_mana = me.IntField(required=True)


class Hero(me.Document):
    meta = {'collection': 'heroes'}

    describtion = me.StringField(max_length=500, required=True)
    name = me.StringField(max_length=100, required=True)
    hp = me.IntField(required=True)
    mana = me.IntField(required=True)
    hp_regen = me.FloatField(required=True)
    mana_regen = me.FloatField(required=True)
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

    describtion = me.StringField(max_length=500, required=True)
    name = me.StringField(max_length=100,required=True)
    damage = me.IntField(required=True)
    magic = me.IntField(required=True)
    hp = me.IntField(required=True)
    hp_regen = me.FloatField(required=True)
    mana = me.IntField(required=True)
    armor = me.IntField(required=True)
    magic_resis = me.IntField(required=True)
    move_speed = me.IntField(required=True)
    damage_speed = me.IntField(required=True)
    money = me.IntField(required=True)


class Tower(me.Document):
    meta = {'collection': 'towers'}

    damage = me.IntField(required=True)
    armor = me.IntField(required=True)
    damage_speed = me.IntField(required=True)
    magic_resis = me.IntField(required=True)
    damage_range = me.FloatField(required=True)
    cost = me.IntField(required=True)

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



