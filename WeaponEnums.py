from enum import Enum
from dataclasses import dataclass
from items import ItemRarity

class WeaponType(Enum):
    ASSAULT_CARBINE = "Assault Carbine"
    ASSAULT_RIFLE = "Assault Rifle"
    BOLT_ACTION = "Bolt-Action Rifle"
    DMR = "Designated Marksman Rifle"
    GL = "Grenade Launcher"
    LMG = "Light Machine Gun"
    ROCKET_LAUNCHER = "Rocket Launcher"
    SHOTGUN = "Shotgun"
    SMG = "Submachine Gun"

class WeaponCaliber(Enum):
    AMMO_9x19MM = "9x19mm Parabellum"
    AMMO_9x39MM = "9x39mm"
    AMMO_5_45x39MM = "5.45x39mm"
    AMMO_5_56x45MM = "5.56x45mm NATO"
    AMMO_7_62x39MM = "7.62x39mm"
    AMMO_7_62x51MM = "7.62x51mm NATO"
    AMMO_12GAUGE = "12 Gauge"
    AMMO_40MM = "40mm Grenade"
    AMMO_4_6x30MM = "4.6x30mm"

class FireMode(Enum):
    SingleShot = "Single Shot"
    SemiAuto = "Semi Auto"
    Burst = "Burst"
    FullAuto = "Full Auto"

@dataclass
class WeaponDataMixin:
    rarity: ItemRarity
    weapon_name: str
    weapon_type: WeaponType
    description: str
    durability: int
    weight: int
    ergonomics: int
    accuracy: int
    recoil: int
    muzzle_velocity: int
    fire_mode: list[FireMode]
    caliber: WeaponCaliber
    fire_rate: int
    effective_distance: int

class Weapon(WeaponDataMixin, Enum):
    #Assault Carbines
    ADAR_2_15 = (ItemRarity.COMMON,"ADAR 2-15",WeaponType.ASSAULT_CARBINE, 
    "A cheap but versatile assault carbine.",
    100, 3267, 60.5, 2.2, 84, 905, [FireMode.SemiAuto], WeaponCaliber.AMMO_5_56x45MM, 800, 500)

    VSK_94 = (ItemRarity.UNCOMMON,"VSK-94",WeaponType.ASSAULT_CARBINE, 
    "A reliable and versatile assault carbine.",
    100, 2992, 54, 4.37, 62, 246, [FireMode.SemiAuto, FireMode.FullAuto], WeaponCaliber.AMMO_9x39MM, 700, 400)

    SR_3M = (ItemRarity.RARE,"SR-3M",WeaponType.ASSAULT_CARBINE, 
    "A very reliable and versatile assault carbine.",
    100, 2593, 70, 5.02, 59, 290, [FireMode.SemiAuto, FireMode.FullAuto], WeaponCaliber.AMMO_9x39MM, 900, 400)

    LONE_STAR_TX_15_DML = (ItemRarity.LEGENDARY,"Lone star TX-15 DML",WeaponType.ASSAULT_CARBINE, 
    "A very very reliable and versatile assault carbine.",
    100, 3702, 34, 1.38, 56, 922, [FireMode.SemiAuto], WeaponCaliber.AMMO_5_56x45MM, 800, 500)

    RFB = (ItemRarity.MYTHIC,"RFB",WeaponType.ASSAULT_CARBINE, 
    "A very super reliable and versatile assault carbine.",
    100, 3606, 50, 1.58, 136, 805, [FireMode.SemiAuto], WeaponCaliber.AMMO_7_62x51MM, 700, 900)

    #Assualt Rifles
    AK_74 = (ItemRarity.COMMON,"AK-74",WeaponType.ASSAULT_RIFLE, 
    "A cheap but versatile assault rifle.",
    100, 3320, 39, 1.99, 85, 906, [FireMode.SemiAuto, FireMode.FullAuto], WeaponCaliber.AMMO_5_45x39MM, 650, 650)



#MOVE ALL THIS INTO THE DATA CLASS
class WeaponName(Enum):

    #ASSAULT RIFLES

    AK_74 = "AK-74"
    AKM = "AKM"
    AS_VAL = "AS VAL"
    M4A1 = "M4A1"
    SA_58 = "SA-58"

    #BOLT-ACTION RIFLES

    AXMC = "AXMC"
    DVL_10 = "DVL-10"
    MARLIN_MXLR = "Marlin MXLR"
    T_5000M = "T-5000M"
    VPO_215 = "VPO-215"

    #DESIGNATED MARKSMAN RIFLES

    SR_25 = "SR-25"
    SVDS = "SVDS"
    G28 = "G28"
    M1A = "M1A"

    #GRENADES LAUNCHERS

    FN40GL = "FN40GL"
    M32A1 = "M32A1"

    #LIGHT MACHINE GUNS

    M60E4 = "M60E4"
    RPK_16 = "RPK-16"
    PKM = "PKM"

    #ROCKET LAUNCHERS

    RSHG2 = "RShG-2"

    #SHOTGUNS

    AA_12_GEN_1 = "AA-12 Gen1"
    M870 = "M870"
    MP_153 = "MP-153"
    TOZ_106 = "TOZ-106"
    SAIGA_12K = "Saiga-12K"

    #SUBMACHINE GUNS

    MP5 = "MP5"
    MP7A1 = "MP7A1"
    MP9 = "MP9"
    VECTOR_45 = "Vector .45"
    SR_2M = "SR-2M"

    #SECONDARY WEAPONS

    BLICKY = "Blicky"
    GLOCK_18C = "Glock 18C" 
    M1911A1 = "M1911A1"



    





