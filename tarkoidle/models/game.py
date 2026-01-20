from tarkoidle.utils.game_time import GameTime


class Game:
    def __init__(self):
        self.time: GameTime = GameTime()

    @property
    def times(self) -> list[str]:
        self.time.update()
        return [self.time.a_str, self.time.b_str]

