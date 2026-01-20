from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any

from tarkoidle.enums.item import ItemVariant
from tarkoidle.enums.skill import SkillVariant
from tarkoidle.enums.trader import TraderVariant


@dataclass
class TaskPrereqs:
    level: int
    reputation: dict[TraderVariant, int]
    tasks: list[Task]
    time: timedelta

@dataclass
class TaskRewards:
    experience: int
    reputation: dict[TraderVariant, int]
    skill_levels: list[tuple[SkillVariant, int]]
    items: list[tuple[ItemVariant, int]]
    # Unlocks can be barter, purchase, craft, achievement
    unlocks: list[Any]  # TODO: find appropriate type

class Task:
    def __init__(self):
        self.trader: TraderVariant
        self.name: str
        self.description: str
        self.subtasks: list[Any]  # TODO: find appropriate type
        self.prereqs: TaskPrereqs
        self.expiration: datetime
        self.rewards: TaskRewards
        self.initial_equipment: list[ItemVariant]
        # self.progress:  # TODO: find a way to track this

