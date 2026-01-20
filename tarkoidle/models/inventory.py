from tarkoidle.enums.item import ItemCategory, ItemVariant
from tarkoidle.models.grid import GridSize


class Inventory:
    def __init__(self, grid: list[GridSize]):
        self.grid: list[GridSize] = grid
        self.item_whitelist: list[ItemVariant | ItemCategory] = []
        self.item_blacklist: list[ItemVariant | ItemCategory] = []

