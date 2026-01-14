import WeaponEnums
from WeaponEnums import WeaponType, WeaponCaliber


class Weapon:
    def __init__(self, name, type: WeaponType, caliber: WeaponCaliber, weight, size):
        self.name = name
        self.type = type
        self.caliber = caliber
        self.weight = weight
        self.size = size


MP7 = Weapon("HK MP7",WeaponType.SMG, WeaponCaliber.AMMO_4_6x30MM, "2.5kg", "Compact")

print(str(MP7.name))
print(str(MP7.type.value))
print(str(MP7.caliber.value))