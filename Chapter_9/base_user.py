"""A set of classes used to represent a base user."""
# This was broken out just for exercise 9-12, it is identical to the user in user.py

class User:
    """Represents a user in the system."""

    def __init__(self, first_name, last_name, age, username):
        """Initalize the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.login_attempts = 0

    def describe_user(self):
        """Prints out a summary of the user's information."""
        print("Summary for the user:")
        print(f"\tFirst Name: {self.first_name}")
        print(f"\tLast Name: {self.last_name}")
        print(f"\tAge: {self.age}")
        print(f"\tUsername: {self.username}")
        print("This is probably some kind of privacy violation!")

    def greet_user(self):
        """Prints a statement greeting the user."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}! " +
            "We hope you have a wonderful day!")

    def increment_login_attempts(self):
        """Increments the number of times a user has attempted to log in by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login attempts to zero."""
        self.login_attempts = 0