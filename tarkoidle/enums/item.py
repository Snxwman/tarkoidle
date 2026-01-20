from dataclasses import dataclass
from enum import Enum, auto


class ItemRarity(Enum):
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    LEGENDARY = auto()
    MYTHIC = auto()

# TODO: Determine how to handle subcategories nicely
class ItemCategory(Enum):
    BARTER = 'Barter'
    EXTRACTION_INTEL = 'Extraction Intel'
    KEY = 'Key'
    KEY_CARD = 'Key Card'
    MEDICAL = 'Medical'
    WEAPON = 'Weapon'
    QUEST = 'Quest'
    INFO = 'Info'
    MAP = 'Map'
    MONEY = 'Money'
    POSTER = 'Poster'
    SPECIAL = 'Special'
    PROVISION = 'Provision'
    INJECTOR = 'Injector'
    CONTAINER = 'Container'
    SECURE_POUCH = 'Secure Pouch'
    DOG_TAG = 'Dog Tag'
    EQUIPMENT = 'Equipment'


@dataclass
class ItemVariantData:
    category: str
    slot: str
    name: str
    rarity: ItemRarity
    weight: int
    sold_by: str
    description: str
    grid_size: int

class ItemVariant(Enum):
    ADAR_2_15 = ''
