# What is the Polymorphism in OOP?
'''
Polymorphism means "multiple forms"
it allows you to use the same interface (method name)
to operate different types of objects, and these objects will
implement different behaviors according to their respective classes.

class method overrides

'''
# super class
class Birds:
    # intializer
    def __init__(self):
        print("There are many types of birds in the world.")

    # class method
    def fly(self):
        print("Many birds can fly and some of them cannot fly!")

# subclass1:
class Sparrow(Birds):
    # we can overrides the superclass's method fly()
    def fly(self):
        print("Sparrow can fly!")

# subclass2:
class Orstich(Birds):
    # we can overrides the superclass's method fly()
    def fly(self):
        print("Ostrich cannot fly!")


# create 3 objects of classes
bird1 = Birds()
sparrow1 = Sparrow()
orstich1 = Orstich()


# caller
for bird in (bird1, sparrow1, orstich1):
    bird.fly() # polymorphism 
    print("#" * 20)