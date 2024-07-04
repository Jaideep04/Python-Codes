# Class definition
class Animal:
    # Class variable
    species = "Unknown"

    # Constructor (Initializer method)
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def make_sound(self):
        pass  # Placeholder for the sound

# Inheritance
class Dog(Animal):
    # Constructor
    def __init__(self, name, age, breed):
        # Calling the parent class constructor
        super().__init__(name, age)
        # Additional subclass-specific variable
        self.breed = breed

    # Overriding the make_sound method
    def make_sound(self):
        return "Woof!"

# Encapsulation
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        # Private variable
        self.__color = color

    # Getter method for the private variable
    def get_color(self):
        return self.__color

    # Setter method for the private variable
    def set_color(self, color):
        self.__color = color

# Polymorphism
def animal_info(animal):
    print(f"Name: {animal.name}, Age: {animal.age}, Species: {animal.species}")
    print(f"Sound: {animal.make_sound()}")

# Creating objects
dog = Dog("Buddy", 3, "Golden Retriever")
cat = Cat("Whiskers", 2, "Gray")

# Accessing class variable
print(f"Dog species: {dog.species}")

# Accessing encapsulated variable using getter method
print(f"Cat color: {cat.get_color()}")

# Modifying encapsulated variable using setter method
cat.set_color("White")

# Using polymorphism to display information
animal_info(dog)
animal_info(cat)
