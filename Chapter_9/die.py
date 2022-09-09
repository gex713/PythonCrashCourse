"""Represents a simple Die for making random choices"""

from random import randint

class Die:
    """A simple class representing a polyhedral die"""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll_die(self):
        """Returns a random number based on the number of sides of the die."""
        print(f"Rolled a {randint(1, self.num_sides)}!")
