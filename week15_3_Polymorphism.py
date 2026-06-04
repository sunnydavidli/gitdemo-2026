# What is the Polymorphism in OOP?
'''
Polymorphism means "multiple forms"
it allows you to use the same interface (method name)
to operate different types of objects, and these objects will
implement different behaviors according to their respective classes.

class method overrides

'''
import time

# 1. Animal speak (basic polymorphism)
# different classes have the same method names

# super class
class Animal:
    # a class attribute
    property = "This is a class attribute of animal"

    # initializer
    def __init__(self, name, speed):
        self.name = name
        # we can make the speed as a priviate attribute
        self._speed = speed 

    # class method: display the object's attribute values
    def __str__(self):
        return '''Animal({0.name}, {0._speed}) is printed
        name = {0.name}
        speed = {0._speed}'''.format(self)
    
    # class method: speak
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    # class method: getSpeedBehavior()
    def getSpeedBehavior(self):
        raise NotImplementedError("Subclasses must implement this method.") 
    

# subclass 1:
class Dog(Animal):
    # initializer
    def __init__(self, name, speed, color, genre, age):
        super().__init__(name, speed) # inheritance from the superclass
        self.color = color
        self.genre = genre
        self.age = age 

    # class method in subclass
    def info(self):
        print("I am a dog, my name is {} and I'm {} years old".format(self.name, self.age))

    # override the class method with polymorphism
    # subclass method: speak
    def speak(self):
        print("Woof!")

    # subclass method: getSpeedBehavior()
    def getSpeedBehavior(self):
        print("The running speed of {} is {}.".format(self.name, self._speed))
        return self._speed


# subclass 1:
class Cat(Animal):
    # initializer
    def __init__(self, name, speed, color, genre, age):
        super().__init__(name, speed) # inheritance from the superclass
        self.color = color
        self.genre = genre
        self.age = age 

    # class method in subclass
    def info(self):
        print("I am a cat, my name is {} and I'm {} years old".format(self.name, self.age))

    # override the class method with polymorphism
    # subclass method: speak
    def speak(self):
        print("Meow!")

    # subclass method: getSpeedBehavior()
    def getSpeedBehavior(self):
        print("The running speed of {} is {}.".format(self.name, self._speed))
        return self._speed


class Manager:
    # initializer
    def __init__(self, animal):
        self.animal = animal
    
    # class method
    def recordTime(self):
        self._t = time.time()
        print("The feeding time for {} is {}.".format(self.animal.name, self._t))
        self.animal.getSpeedBehavior()

    # class method
    def getFeedTime(self):
        return ('%0.f'%(self._t))
    
# main interface to run this program 
if __name__ == '__main__':
    # create 2 objects
    dog1 = Dog("Cute", 5, "Pink", "Miki", 3)
    cat1 = Cat("Flur", 12, "Grey", "Pure", 5)

    Manager(cat1).recordTime()
    print()

    Manager(dog1).recordTime()
    print()


print("this is a demonstration of using the git to track the program change.")
print("HaHa, now I'm using the github remote repository to help me track the code change.")