"""A class that represents simple restaurants."""

class Restaurant:
    """A simple class to represent a restaurant."""

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant {self.name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.name} is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served