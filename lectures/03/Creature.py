class Creature:
    def __init__(self, name):
        self.name = name
        print("Creature " + self.name + " created.")
    def talk(self):
        return "My name is " + self.name + " and I am a Creature" + self.makeSound();
    def makeSound(self):
        return ""
