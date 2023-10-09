class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name}'s coat color is {self.coat_color}")

class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, hunting_skill):
        super().__init__(name, age, coat_color)
        self.hunting_skill = hunting_skill

    def special_skill(self):
        print(f"{self.name} has a hunting skill level of {self.hunting_skill}.")

class Bulldog(Dog):
    def __init__(self, name, age, coat_color, strength):
        super().__init__(name, age, coat_color)
        self.strength = strength

    def show_strength(self):
        print(f"{self.name} has a strength level of {self.strength}.")

dog1 = JackRussellTerrier("Rex", 3, "white", "high")
dog2 = Bulldog("Buddy", 5, "brown", "strong")

dog1.description()
dog1.get_info()
dog1.special_skill()

dog2.description()
dog2.get_info()
dog2.show_strength()