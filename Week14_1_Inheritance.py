# An simple example to review Python OOP inheritance

# superclass: Animal
# subclass: Cat

# define a superclass
class Animal:
    # a class attribute
    property = "This ios a class attribute of animal!"

    # initializer
    def __init__(self, name, speed):
        self.name = name
        # we can further define a private attribute
        self._speed = speed 

    # class method
    def __str__(self):
        return '''Animal({0.name}, {0._speed}) is printed
        name = {0.name}
        speed = {0._speed}'''.format(self)
    
# define a subclass
class Cat(Animal):
    # initializer
    def __init__(self, name, speed, color, genre):
        super().__init__(name, speed)
        self.color = color
        self.genre = genre

# Now, we can create an object (instance) of subclass
cat1 = Cat('CuteBoy', 8, 'White', 'CatGenre')
print(cat1)