import math
from weather_api import read_weather

class Targets:
    """
    this class represent Targets
    """
    IL_LAT = 31.79592425
    IL_LON = 35.211980759695

    def __init__(self, target_city: str, lat: float, lon: float, priority: int):
        self.__target_city = target_city
        self.__lat = lat
        self.__lon = lon
        self.__priority = priority
        self.__weather = read_weather(self.__target_city)
        self.__distance = self.haversine_distance()
        self.__weather_rank = self.weather_score(self.weather)

    def haversine_distance(self):
        """
        # Function to calculate the distance between two coordinates using the Haversine formula
        :param lon1:
        :return:
        """
        r = 6371.0  # Radius of the Earth in kilometers
        # Convert degrees to radians
        lat1_rad = math.radians(self.__lat)
        lon1_rad = math.radians(self.__lon)
        lat2_rad = math.radians(Targets.IL_LAT)
        lon2_rad = math.radians(Targets.IL_LON)
        # Calculate differences between the coordinates
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        # Apply Haversine formula
        a = (math.sin(dlat / 2) ** 2
             + math.cos(lat1_rad) * math.cos(lat2_rad)
             * math.sin(dlon /  2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        # Calculate the distance
        distance = r * c
        return distance

    def weather_score(self, weather):
        if weather["main"] == "Clear":
            return 1.0
        elif weather["main"] == "Clouds":
            return 0.7
        elif weather["main"] == "Rain":
            return 0.4
        elif weather["main"] == "Stormy":
            return 0.2
        else:
            return 0

    @property
    def distance(self):
        return self.__distance

    @property
    def city(self):
        return self.__target_city

    @property
    def weather(self):
        return self.__weather

    @property
    def weather_rank(self):
        return self.__weather_rank

    @property
    def priority(self):
        return self.__priority

    def __str__(self):
        return f'{self.__target_city}: {self.__weather_rank}: {self.__weather}: {self.__distance}'
if __name__ == '__main__':
    iran = Targets('IR', 35.6892523, 51.3896004, 5)
    print(iran.distance)


