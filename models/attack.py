from models.aircraft import Aircraft
from models.pilots import Pilot
from models.targets import Targets
# from Math import abs

class Attack:

    weights = {
        "distance": 0.20,
        "aircraft_type": 0.25,
        "pilot_skill": 0.25,
        "weather_conditions": 0.20,
        "execution_time": 0.10
    }

    def __init__(self, aircraft, pilots, target):
        self.aircraft: Aircraft = aircraft
        self.pilots: Pilot = pilots
        self.target: Targets = target
        self.rank = abs(self.calculate_renk())

    def calculate_renk(self):
        distance = self.target.distance
        aircraft_range = self.aircraft.fuel_capacity / self.aircraft.speed
        pilot_rank = self.pilots.skill
        weather = self.target.weather_rank
        time_completed = distance / aircraft_range
        priority_target = self.target.priority

        result = (aircraft_range + pilot_rank + weather + priority_target - time_completed - distance) / 6

        return result

    def __str__(self):
        return f'{self.aircraft} - {self.pilots} - {self.target} - {self.rank}'

