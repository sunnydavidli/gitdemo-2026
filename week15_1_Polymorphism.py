# What is the Polymorphism in OOP?
'''
Polymorphism means "multiple forms"
it allows you to use the same interface (method name)
to operate different types of objects, and these objects will
implement different behaviors according to their respective classes.

'''

# 1. Animal speak (basic polymorphism)
# different classes have the same method names

# super class
class Animal:
    # initializer
    def __init__(self):
        pass

    # class method: speak
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")
    

# 2 subclasses
class Dog(Animal):
    # subclass method: speak
    def speak(self):
        return "Woof!"
    

class Cat(Animal):
    # subclass method: speak
    def speak(self):
        return "Meow!"


def animal_sound(animal: Animal):
    print(animal.speak())


# caller
dog1 = Dog() # create an object of class
cat1 = Cat()

animal_sound(dog1) # polymorphism
animal_sound(cat1)