import os
from random import randint, sample
import logging
from mongoengine import *
from filler_creatures import creatures, abilities

logging.basicConfig(level=logging.DEBUG)


class Ability(Document):
    name = StringField(required=True, unique=True)
    effect_stat = IntField()
    effect_status = StringField()

    description = StringField()

    meta = {'strict': False}


class Creature(Document):
    name = StringField(required=True, unique=True)
    image = StringField()

    hp = IntField(default=50, required=True)
    attack = IntField(required=True)
    defense = IntField(required=True)
    speed = IntField(required=True)
    ability = ReferenceField(Ability)
    description = StringField()
    lore = StringField()

    meta = {'strict': False}

    def __repr__(self):
        ability_name = self.ability.name if self.ability else "No Ability yet"
        return f"<Creature {self.name} - Atk {self.attack}: {ability_name}>"


if os.getenv("USE_LOCAL"):
    connect("Creatures")
    logging.debug("Running on local database.")
else:
    connect(host=os.getenv("CREATURE_DEN_DATABASE_URL"))
    logging.debug("Running on the cloud.")

Creature.drop_collection()
Ability.drop_collection()

# Your code goes here
ire = Abilities(name = "Sun of SoaRa", effect = 15, description ="The sun of the god, SoaRa burns its enemies with its powerful blade to expell its enemies of Nefhakara")
Water = Abilities(name = "Watter Wash", effect = 22, description ="This floods the field and attacking your opponent")
Water_2 = Abilities(name = "Wright Hook", effect = 44, description ="Your opponent gives a deadly right hook and confusing him")
Water_3 = Abilities(name = "Shorpedo", effect = 50, description ="Charges at your enemy exploding and dealing a huge amount of damage")
Water_4 = Abilities(name = "Shark slam", effect = 64, description ="Slams the opponent into the depths of the sea")
Water_five = Abilities(name = "Throne of thorns", effect = 99, description ="Sends thorns out of the sea")
Batalla =Abilities(name = "Blood Charge", effect = 55, discription = " The Charge of Blood Charges at the at the enemy and slams him into the ground")
Phantasm = Abilities(name = "Prism of Hel", effect = 88, discription = " Draksoul throws The shards of the lost souls and steals your HP ")
Phantasm_2 = Abilities(name = "Minions of Hel", effect = 90, discription = "The Minions of the 2nd Dynasty rise against your foes and defend their Lord of Hel")
Phantasm_3 = Abilities(name = "Hound of Hel", effect = 69, discription = "When in low health it will heal it self and nearby  allies  ")
Gust =Abilities(name = "Wind gust", effect = 33, description = "Creates high winds making the opponent lose accuracy and hurt their allies")
Fetcher_souls =Abilities(name = "Fetcher of Souls", effect = 77, description =" Fetcher pf souls retrive a huge amount from the enemy and heals your character")
Reptile = Abilities("Scale Hide", effect = 89, description = "harden the scales and when broken replaces it by the new scales it already has")
Xin = Abilities("Guardian of the Palace", effect = 100, description= "I will give health and shield to the teamates of  your party")
Tomb_Guard = Abilities(name = "Tomb Guardian", effect = 100 , description = "For 4 turns the character will defend a member of your party")
Crystal = Abilities(name ="Crystal Shards", effect = 87, description = "The Priest will throw shards of magical crystals and cause harm the closest member of the party it is nexto")
Sand_sweep = Abilities(name =" Desert combat", effect = 120 , description = " Train in the arts of desert combat BoneChakal will cause a heavy blow against his foes")
Ancestors = Abilities(name = "Dynasty Ancestors", effect = 4000, description = " Your foes will all will be eliminated if all members of your party have perish")
Dynasty =Abilities(name = "King of Kings", effect = 100, description =" All charcters will recive king status meaning all creatures of the party have full defence and full attack")


D_one =Dynasties(name= "Sharnado", health=2000,attack=78, defence= 67)
D_two =Dynasties(name= "Hook Jaw", health=1400,attack=83, defence= 55)
D_three =Dynasties(name= "AquaBite", health=9000,attack=84, defence= 88)
D_Four =Dynasties(name= "Bloat", health=2500,attack=95, defence= 90)
D_five = Dynasties(name= "King Spikey", health=15000,attack=95, defence= 90)

DD_one =Dynasties(name= "Master BloodHorns", health=4000,attack=87, defence= 50)
DD_two =Dynasties(name= "Draksoul", health=3000,attack=53, defence= 63)
DD_three =Dynasties(name= "Shaman RedTail", health=16000,attack=77, defence= 87)
DD_four =Dynasties(name= "Lord Phantamas ", health=12000,attack=58, defence= 100)
DD_five =Dynasties(name= "Hounth Fantasma", health=44000,attack=91, defence= 89)

DDD_one = Dynasties(name ="Lord Twotales",health =9933, attack = 55, defence = 54)
DDD_two = Dynasties(name = "King Djaf", health = 15000, atack = 55, defence = 65)
DDD_three = Dynasties(name ='Gran Coyote',health = 40000, attack = 25, defence = 69)
DDD_four = Dynasties(name ="Cheif Choquaxul",health= 50000,attack =44, defence = 30)
DDD_five = Dynasties(name ="Xin Fox", health =120000, attack = 78, defence= 78)

DDDD_one = Dynasties(name = "Bonechakal", health = 40000, attack = 55, defence = 87)
DDDD_two = Dynasties(name = "Prince Anubite", health = 600000, attack = 78, defence = 97)
DDDD_three =Dynasties(name = "Priest Kobrox", health = 70000, attack = 56, defence= 78)
DDDD_four = Dynasties(name ="Cuyo", health = 30000, attack = 60, defence =90)
DDDD_five = Dynasties(name = "Fouron", health = 500000, attack = 87, defence = 90)

#----------------Dynasty 1--------------------
D_one.save()
D_two.save()
D_three.save()
D_Four.save()
D_five.save()
# ----------Dynasty 2----------------------
DD_one.save()
DD_two.save()
DD_three.save()
DD_four.save()
DD_five.save()
#---------------Dynasty 3------------------
DDD_five.save()
DDD_four.save()
DDD_three.save()
DDD_two.save()
DDD_one.save()

#---------------------------Dynasty 4 ------------------------------
DDDD_five.save()
DDDD_four.save()
DDDD_three.save()
DDDD_two.save()
DDDD_one.save()

#-------------------------------Abilities saved-----------------------------
fire.save()
Water.save()
Water_2.save()
Water_3.save()
Water_4.save()
Water_five.save()
Batalla.save()
Phantasm.save()
Phantasm_2.save()
Phantasm_3.save()
Gust.save()
Fetcher_souls.save()
Reptile.save()
Xin.save()
Tomb_Guard.save()
Sand_sweep.save()
Crystal.save()
Ancestors.save()
Dynasty.save()

# ---------------------- I don't know what to call. its just assigning the abilities to the creatures ---------------------------------------
D_one.abilities = Water
D_two.abilities =Water_2
D_three.abilities = Water_3
D_Four.abilities = Water_4
D_five.abilities =Water_five

DD_one.abilities = Batalla
DD_two.abilities = Phantasm
DD_three.abilities = Phantasm_2
DD_five.abilities = Phantasm_3

DDD_one.abilities = Gust
DDD_two.abilities = Fetcher_souls
DDD_three.abilities = fire
DDD_four.abilities =Reptile
DDD_five.abilities = Xin

DDDD_one.abilities = Sand_sweep
DDDD_two.abilities = Tomb_Guard
DDDD_three.abilities = Crystal
DDDD_four.abilities = Ancestors
DDDD_five.abilities = Dynasty
# Generating filler creatures

#find already used images

pics_already_used = Creature.objects().distinct("image")

all_pics = [str(n)for n in range(1, 829)]

unused_pics = list(set(all_pics).difference(pics_already_used))

for each_filler_creature, each_ability in zip(creatures, abilities):
    creature_name = each_filler_creature
    ability_name = each_ability

    creature_description = creatures[creature_name]["description"]
    creature_lore = creatures[creature_name]["lore"]
    ability_description = abilities  [ability_name]

    hp = randint(1, 100)

    attack = randint(1, 100)

    defense = randint(1, 100)

    speed = randint(1, 100)

    image = sample(unused_pics, 1)[0]
    c = Creature(name=creature_name, description=creature_description,
                 hp=hp, attack=attack, defense=defense, speed=speed,
                  lore=creature_lore)

    a = Ability(name=ability_name,description=ability_description)

    a.save()
    c.ability = a
    c.save()
    pass


pass


def creature():
    return None