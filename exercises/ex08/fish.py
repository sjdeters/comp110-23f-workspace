"""File to define Fish class."""


class Fish:
    """Fish in the river."""

    age: int

    def __init__(self, age_init: int = 0):
        """Initializes our fish."""
        self.age = age_init
        return None
    
    def one_day(self):
        """Models how the population of fish updates day-to-day."""
        self.age += 1
        return None