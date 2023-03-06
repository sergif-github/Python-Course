# Inheritance
print('''Inheritance''')
# Inheritance is a way to form new classes using classes that have already been defined
class Dog:
    # An attribute is a characteristic of an object

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # Redefinition
    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

    def speak(self):
        return self.name + ' says Woof!'


d = Dog()
d.whoAmI()
d.bark()
print(d.speak())
