from dataclasses import dataclass

from tarkoidle.models.hideout import Hideout
from tarkoidle.models.skill import Skill
from tarkoidle.models.stash import Stash


@dataclass
class CharacterSkills:
    endurance: Skill
    health: Skill
    metabolism: Skill
    strength: Skill
    stress_resistance: Skill
    vitality: Skill

    aim_drills: Skill
    assault_rifles: Skill
    # TODO: add other weapon types
    throwables: Skill

    covert_movement: Skill
    crafting: Skill
    hideout_management: Skill
    mag_drills: Skill
    search: Skill
    surgery: Skill
    weapon_maintenance: Skill

    attention: Skill
    charisma: Skill
    intellect: Skill
    perception: Skill


@dataclass
class CharacterTraderRep:
    prapor: int = 50
    therapist: int = 50
    fence: int = 0
    skier: int = 50
    peacekeeper: int = 50
    mechanic: int = 50
    ragman: int = 50
    jeager: int = 50
    ref: int = 50
    lightkeeper: int = 0
    btr_driver: int = 0


class CharacterPMC:
    def __init__(self):
        self.username: str
        self.level: int = 1
        self.prestige_level: int = 0
        self.experience: int = 0
        self.stash: Stash
        self.hideout: Hideout
        self.skills: CharacterSkills
        self.tasks: CharacterTasks
        self.trader_rep: CharacterTraderRep = CharacterTraderRep()
        # self.achievements: CharacterAchievements

        # self.raid_log: list[RaidResult]
        # self.meta: CharacterMetadata


class CharacterScav: ...
