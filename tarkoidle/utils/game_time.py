from datetime import datetime, timedelta
from typing import final
from zoneinfo import ZoneInfo


@final
class GameTime:
    a: int
    b: int
    _last_updated: datetime
    _min_update_delta: int
    a_str: str = ''
    b_str: str = ''
    TIMEZONE = 'Europe/Moscow'
    SPEEDUP = 8 # Multiple of real world minutes to in game minutes

    def __init__(self):
        now = datetime.now(tz=ZoneInfo(GameTime.TIMEZONE))
        GameTime.a = now.hour * 100 + now.minute
        GameTime.b = (GameTime.a + 1200) % 2400
        GameTime.update_strs()
        GameTime._last_updated = now
        GameTime._min_update_delta = int(60 / GameTime.SPEEDUP)

    @staticmethod
    def update_strs():
        a_str = f'{GameTime.a:04d}'
        b_str = f'{GameTime.b:04d}'
        GameTime.a_str = f'{a_str[0:2]}:{a_str[2:4]}'
        GameTime.b_str = f'{b_str[0:2]}:{b_str[2:4]}'

    @staticmethod
    def update():
        now = datetime.now(tz=ZoneInfo(GameTime.TIMEZONE))
        delta: timedelta = now - GameTime._last_updated

        if delta.seconds < GameTime._min_update_delta:
            return

        # Calculate the real world time delta
        delta_hours = int(delta.seconds / 3600)
        delta_mins = (delta.seconds - delta_hours * 3600) / 60

        # Account for time speedup
        delta_game_mins = round(delta_mins * GameTime.SPEEDUP)
        # Add overflowed hours when spedup minutes crosses an hour boundary
        delta_game_hours = delta_hours * GameTime.SPEEDUP + int(delta_game_mins / 60)
        # Only keep the remaining spedup minutes less than an hour
        delta_game_mins %= 60

        cur_game_mins = GameTime.a % 100
        # Add overflowed hours when adding new minutes to current minutes crosses an hour boundary
        delta_game_hours += int((cur_game_mins + delta_game_mins) / 60)

        # Calculate how many minutes into the hour (in game) the new time is
        new_game_mins = (cur_game_mins + delta_game_mins) % 60

        if delta_game_hours > 0 or delta_game_mins > 0: 
            GameTime.a = ((GameTime.a - GameTime.a % 100) + delta_game_hours * 100) % 2400 + new_game_mins
            GameTime.b = (GameTime.a + 1200) % 2400
            GameTime.update_strs()
            GameTime._last_updated = now

        if GameTime.a < 0 or GameTime.b < 0 or GameTime.a > 2359 or GameTime.b > 2359:
            err_msg = 'Error calculating game time'
            raise ValueError(err_msg)
