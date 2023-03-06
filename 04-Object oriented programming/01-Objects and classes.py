# OBJECTS AND CLASSES
print('''OBJECTS AND CLASSES''')
print('''In Python, everything is an object. We can use type() to check the type of object something is''')

print(type(1))
print(type([]))
print(type(()))
print(type({}))

#To create our own objects we use class

class Animal:
    def __init__(self):
        print("Animal created")

    # A method is an operation we can perform with the object
    def setName(self, new_name):
        self.name = new_name

    def getName(self):
        return self.name
    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


print('''An instance is a specific object created from a particular class''')
sam = Animal()
print(type(sam))

