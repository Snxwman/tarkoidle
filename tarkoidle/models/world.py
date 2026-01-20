from time import time

from tarkoidle.enums.weather import WeatherVariant


class GameWorld:
    def __init__(self):
        self.time_1: time
        self.time_2: time
        self.weather: WeatherVariant
