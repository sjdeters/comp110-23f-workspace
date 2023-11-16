"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730660578"


class River:
    """Our river."""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears?"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """As animals age, they should be removed from the river."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.fish = new_fish
        self.bears = new_bears
        return None
    
    def remove_fish(self, amount: int):
        """Removes amount many fish from the river."""
        for x in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Simulates a bear eating fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Checks to see if the bear is hungry."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0: 
                new_bears.append(bear)
        self.bears = new_bears
        return None
        
    def repopulate_fish(self):
        """Models the reproduction of fish."""
        num_pairs: int = len(self.fish) // 2
        i: int = 0
        while i < num_pairs:
            j: int = 0
            while j < 4:
                self.fish.append(Fish())
                j += 1
            i += 1
        return None
    
    def repopulate_bears(self):
        """Models the reprodution of bears."""
        num_pairs: int = len(self.bears) // 2
        i: int = 0
        while i < num_pairs:
            self.bears.append(Bear())
            i += 1
        return None
    
    def view_river(self):
        """Prints the river status."""
        current_day: int = self.day
        num_fish: int = len(self.fish)
        num_bears: int = len(self.bears)
        print(f"~~~ Day {current_day}: ~~~")
        print(f"Fish population: {num_fish}")
        print(f"Bear population: {num_bears}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self): 
        """Simulates one week of life in the river."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1