from dataclasses import dataclass

from tarkoidle.enums.skill import SkillVariant


@dataclass
class Skill:
    data: SkillVariant
    name: str
    level: int = 0
    experience: int = 0
    elite: bool = False

