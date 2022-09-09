"""A set of classes that can be used to represent an Admin user."""
# This was broken out just for exercise 9-12
from base_user import User

class Admin(User):
    """Admin is a super user and has particular privileges."""

    def __init__(self, first_name, last_name, age, username):
        super().__init__(first_name, last_name, age, username)
        self.privileges = Privileges()


class Privileges:
    """The privileges that can be available."""
    def __init__(self, privileges=["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def show_privs(self):
        """Prints out all the available privileges."""
        print("The following privileges are available:")
        for priv in self.privileges:
            print(f"\t{priv.title()}")
