import math


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
        self.__distance = self.haversine_distance()

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

    @property
    def distance(self):
        return self.__distance


if __name__ == '__main__':
    iran = Targets('IR', 35.6892523, 51.3896004, 5)
    print(iran.distance)
