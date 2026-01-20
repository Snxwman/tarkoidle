from tarkoidle.models.item import Item


class PlayerInventory:
    def __init__(self) -> None:
        self.headset: Item | None = None
        self.head: Item | None = None
        self.face: Item | None = None
        self.eyes: Item | None = None
        self.armor: Item | None = None
        self.primary_weapon: Item | None = None
        self.secondary_weapon: Item | None = None
        self.side_arm: Item | None = None
        self.rig: Item | None = None
        self.pockets: Item | None = None
        self.backpack: Item | None = None
        self.secure_pouch: Item | None = None
        self.special_slots_1: 

