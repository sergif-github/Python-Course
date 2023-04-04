# Polymorphism
print('''Polymorphism''')
'''Polymorphism refers to the way in which different object classes can share the same method name,
 and those methods can be called from the same place even though a variety of different objects might be passed in'''

class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!'


c = Cat()
print(c.speak())
print(c.speak())


#An abstract class is one that never expects to be instantiated

class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def speak(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):

    def speak(self):
        return self.name + ' says Woof!'


class Cat(Animal):

    def speak(self):
        return self.name + ' says Meow!'


dog = Dog('Fido')
cat = Cat('Isis')

print(dog.speak())
print(cat.speak())