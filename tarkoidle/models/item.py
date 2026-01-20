from tarkoidle.models.grid import GridSize
from tarkoidle.models.inventory import ItemInventory


class Item:
    def __init__(self) -> None:
        self.grid: list[GridSize] = []  # This is a list to handle items that can be expanded/contracted
        self.inventory: ItemInventory | None = None
