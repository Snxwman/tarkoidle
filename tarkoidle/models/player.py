from dataclasses import dataclass
from datetime import datetime

from tarkoidle.config.player import PlayerConfig
from tarkoidle.discord.user import DiscordUser
from tarkoidle.models.character import CharacterPMC, CharacterScav
from tarkoidle.twitch.user import TwitchUser


@dataclass
class PlayerMetadata:
    account_created: datetime


@dataclass
class PlayerModeration:
    timedout: bool = False
    timeout_reason: str | None = None  # TODO: Make a list of reason presets with custom message option.
    timeout_start: datetime | None = None
    timeout_end: datetime | None = None
    banned: bool = False
    ban_reason: str | None = None  # TODO: Make a list of reason presets with custom message option.
    ban_start: datetime | None = None
    ban_end: datetime | None = None
    flea_ban: bool = False
    flea_ban_reason: str | None = None  # TODO: Make a list of reason presets with custom message option.
    flea_ban_start: datetime | None = None
    flea_ban_end: datetime | None = None


class Player:
    def __init__(self):
        self.discord: DiscordUser  # TODO: impl
        self.twitch: TwitchUser  # TODO: impl
        self.pmc: CharacterPMC  # TODO: impl
        self.scav: CharacterScav  # TODO: impl
        self.meta: PlayerMetadata  # TODO: impl
        self.config: PlayerConfig  # TODO: impl
        self.moderation: PlayerModeration = PlayerModeration()
