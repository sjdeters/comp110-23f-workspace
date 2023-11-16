"""File to define Bear class?"""


class Bear:
    """Bears living by the river."""
    age: int
    hunger_score: int

    def __init__(self, age_init: int = 0, hunger_init: int = 0):
        """Initializes our Bears."""
        self.age = age_init
        self.hunger_score = hunger_init
        return None
    
    def one_day(self):
        """Models how the population of bears updates day-to-day."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int): 
        """Models a bear eating a fish."""
        self.hunger_score += num_fish