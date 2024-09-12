class Pilot:
    """
    this class represent pilots
    """

    def __init__(self, name: str, skill: int):
        self.name = name
        self.skill = skill

    def __str__(self):
        return f'{self.name} {self.skill}'