class Aircraft:
    """

    """

    def __init__(self, f_type: str, speed: int, fuel_capacity: int):
        self.f_type = f_type
        self.speed = speed
        self.fuel_capacity = fuel_capacity

    def __str__(self):
        return f'{self.f_type} {self.speed} {self.fuel_capacity}'