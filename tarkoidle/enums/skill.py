# ruff: noqa: PIE796  # TODO: Remove
from dataclasses import dataclass
from enum import Enum, unique
from typing import final

import tarkoidle.data.skill as constants


class SkillCategory(Enum):
    PHYSICAL = 'Physical'
    COMBAT = 'Combat'
    PRACTICAL = 'Practical'
    MENTAL = 'Mental'

@dataclass
class SkillVariantData:
    category: SkillCategory
    description: str = '' # TODO: Remove default
    effects: list[str] = []  # TODO: Remove default
    effects_elite: list[str] = []  # TODO: Remove default
    increased_by: list[str] = []  # TODO: Remove default

@final
@unique
class SkillVariant(SkillVariantData, Enum):
    ENDURANCE = (
        SkillCategory.PHYSICAL,
        constants.ENDURANCE_DESCRIPTION,
        constants.ENDURANCE_EFFECTS,
        constants.ENDURANCE_EFFECTS_ELITE,
        constants.ENDURANCE_INCREASED_BY,
    )
    HEALTH = (
        SkillCategory.PHYSICAL,
        constants.HEALTH_DESCRIPTION,
        constants.HEALTH_EFFECTS,
        constants.HEALTH_EFFECTS_ELITE,
        constants.HEALTH_INCREASED_BY,
    )
    METABOLISM = (
        SkillCategory.PHYSICAL,
        constants.METABOLISM_DESCRIPTION,
        constants.METABOLISM_EFFECTS,
        constants.METABOLISM_EFFECTS_ELITE,
        constants.METABOLISM_INCREASED_BY,
    )
    STRENGTH = (
        SkillCategory.PHYSICAL,
        constants.STRENGTH_DESCRIPTION,
        constants.STRENGTH_EFFECTS,
        constants.STRENGTH_EFFECTS_ELITE,
        constants.STRENGTH_INCREASED_BY,
    )
    STRESS_RESISTANCE = (
        SkillCategory.PHYSICAL,
        constants.STRESS_RESISTANCE_DESCRIPTION,
        constants.STRESS_RESISTANCE_EFFECTS,
        constants.STRENGTH_EFFECTS_ELITE,
        constants.STRESS_RESISTANCE_INCREASED_BY,
    )
    VITALITY = (
        SkillCategory.PHYSICAL,
        constants.VITALITY_DESCRIPTION,
        constants.VITALITY_EFFECTS,
        constants.VITALITY_EFFECTS_ELITE,
        constants.VITALITY_INCREASED_BY,
    )

    AIM_DRILLS = (SkillCategory.COMBAT)
    ASSAULT_RIFLES = (SkillCategory.COMBAT)
    BOLT_ACTION_RIFLES = (SkillCategory.COMBAT)
    # TODO: add other weapon types
    THROWABLES = (SkillCategory.COMBAT)
    TROUBLESHOOTING = (SkillCategory.COMBAT)

    COVERT_MOVEMENT = (SkillCategory.PRACTICAL)
    CRAFTING = (SkillCategory.PRACTICAL)
    HIDEOUT_MANAGEMENT = (SkillCategory.PRACTICAL)
    MAG_DRILLS = (SkillCategory.PRACTICAL)
    SEARCH = (SkillCategory.PRACTICAL)
    SURGERY = (SkillCategory.PRACTICAL)
    WEAPON_MAINTENANCE = (SkillCategory.PRACTICAL)

    ATTENTION = (SkillCategory.MENTAL)
    CHARISMA = (SkillCategory.MENTAL)
    INTELLECT = (SkillCategory.MENTAL)
    PERCEPTION = (SkillCategory.MENTAL)

