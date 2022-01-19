from Creature import Creature

class Dog(Creature):
    def __init__(self, name):
        super().__init__(name)
    def makeSound(self):
        return ": woof."
