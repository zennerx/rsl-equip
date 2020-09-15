from mainapp.Models.user_data import User
from mainapp.Models.equipment_data import *
from mainapp.Models.hero_data import *
from mainapp import db_session

def import_static_data():
    user = User('Luke', 'Croteau', 'Luke Croteau', 'luke.j.croteau@gmail.com', 'male', '114036129857079136644', 
                'https://plus.google.com/114036129857079136644',
                'https://lh6.googleusercontent.com/-E5OobdSibTQ/AAAAAAAAAAI/AAAAAAAAAEg/qkS6vHzpWm4/photo.jpg',
                '1206765207'
                )
    user.is_admin = True
    db_session.add(user)

    db_session.commit()

    hp = StatTypes(name='HP', flat=True)
    db_session.add(hp)
    hppct = StatTypes(name='HP%', flat=False)
    db_session.add(hppct)
    attack = StatTypes(name='ATK', flat=True)
    db_session.add(attack)
    atkpct = StatTypes(name='ATK%', flat=False)
    db_session.add(atkpct)
    defense = StatTypes(name='DEF', flat=True)
    db_session.add(defense)
    defpct = StatTypes(name='DEF%', flat=False)
    db_session.add(defpct)
    speed = StatTypes(name='SPEED', flat=True)
    db_session.add(speed)
    critrate = StatTypes(name='C.RATE%', flat=False)
    db_session.add(critrate)
    critdmg = StatTypes(name='C.DMG%', flat=False)
    db_session.add(critdmg)
    resist = StatTypes(name='RESIST', flat=True)
    db_session.add(resist)
    accuracy = StatTypes(name='ACC', flat=True)
    db_session.add(accuracy)

    weapon = ArtifactTypes(name='Weapon')
    db_session.add(weapon)
    helmet = ArtifactTypes(name='Helmet')
    db_session.add(helmet)
    shield = ArtifactTypes(name='Shield')
    db_session.add(shield)
    gloves = ArtifactTypes(name='Gloves')
    db_session.add(gloves)
    chest = ArtifactTypes(name='Chest')
    db_session.add(chest)
    shoes = ArtifactTypes(name='Shoes')
    db_session.add(shoes)
    ring = ArtifactTypes(name='Ring')
    db_session.add(ring)
    amulet = ArtifactTypes(name='Amulet')
    db_session.add(amulet)
    banner = ArtifactTypes(name='Banner')
    db_session.add(banner)

    db_session.commit()

    a = ArtifactSets(name='Life', count_for_bonus=2, bonus_stat_1=hppct, bonus_value_1=15, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Offense', count_for_bonus=2, bonus_stat_1=atkpct, bonus_value_1=15, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Defense', count_for_bonus=2, bonus_stat_1=defpct, bonus_value_1=15, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Speed', count_for_bonus=2, bonus_stat_1=speed, bonus_value_1=12, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Critical Rate', count_for_bonus=2, bonus_stat_1=critrate, bonus_value_1=12, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Crit Damage', count_for_bonus=2, bonus_stat_1=critdmg, bonus_value_1=20, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Accuracy', count_for_bonus=2, bonus_stat_1=accuracy, bonus_value_1=40, bonus_flat_1=True)
    db_session.add(a)
    a = ArtifactSets(name='Resistance', count_for_bonus=2, bonus_stat_1=resist, bonus_value_1=40, bonus_flat_1=True)
    db_session.add(a)
    a = ArtifactSets(name='Lifesteal', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Fury', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Daze', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Cursed', count_for_bonus=2)
    db_session.add(a)
    a = ArtifactSets(name='Frost', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Frenzy', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Regeneration', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Immunity', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Shield', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Relentless', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Savage', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Destroy', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Stun', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Toxic', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Taunting', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Retaliation', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Avenging', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Stalwart', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Reflex', count_for_bonus=4)
    db_session.add(a)
    a = ArtifactSets(name='Curing', count_for_bonus=2)
    db_session.add(a)
    a = ArtifactSets(name='Cruel', count_for_bonus=2, bonus_stat_1=atkpct, bonus_value_1=15, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Immortal', count_for_bonus=2, bonus_stat_1=hppct, bonus_value_1=15, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Divine Offense', count_for_bonus=2, bonus_stat_1=atkpct, bonus_value_1=15, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Divine Critical Rate', count_for_bonus=2, bonus_stat_1=critrate, bonus_value_1=12, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Divine Life', count_for_bonus=2, bonus_stat_1=hppct, bonus_value_1=15, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Divine Speed', count_for_bonus=2, bonus_stat_1=speed, bonus_value_1=12, bonus_flat_1=False)
    db_session.add(a)
    a = ArtifactSets(name='Swift Parry', count_for_bonus=4, bonus_stat_1=speed, bonus_value_1=18, bonus_flat_1=False, bonus_stat_2=critdmg, bonus_value_2=30, bonus_flat_2=False)
    db_session.add(a)
    a = ArtifactSets(name='Deflection', count_for_bonus=4, bonus_stat_1=hppct, bonus_value_1=20, bonus_flat_1=False, bonus_stat_2=defense, bonus_value_2=20, bonus_flat_2=False)
    db_session.add(a)

    db_session.commit()

    monster = Hero(name='Miscreated Monster', hero_type='Support', hp=22965, attack=958, defense=815, speed=95, critrate=15, critdmg=50, resist=45, accuracy=0)
    db_session.add(monster)