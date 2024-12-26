class User:

    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name


    def first_name(self):
        print(self.firstname)


    def last_name(self):
        print(self.lastname)


    def Full_name(self):
        print(f"{self.firstname} {self.lastname}")

