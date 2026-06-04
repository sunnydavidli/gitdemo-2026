# An simple example to review Python OOP inheritance and polymorphisim

# superclass: Animal
# subclass: Cat, Dog

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
    def __init__(self, name, speed, color, genre, age):
        super().__init__(name, speed)
        self.color = color
        self.genre = genre
        self.age = age

    # a class method in the subclass Cat
    def info(self):
        print("I am a Cat, my name is {} and I'm {} years old.".format(self.name, self.age))

    # a class method
    def make_sound(self):
        print("miaomiao")

# define a subclass
class Dog(Animal):
    # initializer
    def __init__(self, name, speed, color, genre, age):
        super().__init__(name, speed)
        self.color = color
        self.genre = genre
        self.age = age

    # a class method in the subclass Dog
    def info(self):
        print("I am a Dog, my name is {} and I'm {} years old.".format(self.name, self.age))

    # a class method
    def make_sound(self):
        print("BarkBark, woo, woo...")

    

# Now, we can create an object (instance) of subclass
cat1 = Cat('CuteBoy', 8, 'White', 'CatGenre', 3)
dog1 = Dog('Flurfy', 10, 'Black', 'PureDog', 5)

# we use the polymorphism to call the sublcass methods: info(), make_sound() for different objects
for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    print("*"*50)
    print()

