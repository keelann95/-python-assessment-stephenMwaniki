
class Animal:
    # Class variables shared by all Animal (and subclass) instances
    species = "Animal Kingdom"
    counter = 0  # tracks total number of instances created

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        self.__age = 0  
        Animal.counter += 1  # increment every time an instance is made

    def speak(self):
        """Prints the animal's name and the sound it makes."""
        print(f"{self.name} says {self.sound}")

    # Getter for the private __age attribute
    def get_age(self):
        return self.__age

    # Setter for the private __age attribute, with basic validation
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative. Ignoring invalid value.")


class Dog(Animal):
    """Dog is a subclass of Animal - demonstrates inheritance."""

    def __init__(self, name):
        # Dogs always say "Woof", so we set that automatically
        super().__init__(name, sound="Woof")

    def speak(self):
        """Overrides Animal's speak() with dog-specific behaviour."""
        print(f"{self.name} the dog barks: {self.sound}!")


# c. Creating at least two Animal instances and calling speak()
animal1 = Animal("Generic Cat", "Meow")
animal2 = Animal("Generic Cow", "Moo")

print("c. Basic Animal instances:")
animal1.speak()
animal2.speak()

# e. Demonstrating inheritance with the Dog subclass
dog1 = Dog("Rex")
print("\ne. Inheritance demo (Dog subclass):")
dog1.speak()

# d. Class variable counter tracking total instances
print("\nd. Total Animal instances created so far:", Animal.counter)

# f. Encapsulation: using getter/setter for the private __age attribute
print("\nf. Encapsulation demo:")
print("   Rex's age before setting:", dog1.get_age())
dog1.set_age(3)
print("   Rex's age after set_age(3):", dog1.get_age())
dog1.set_age(-5)  # invalid, setter should reject this
print("   Rex's age after an invalid set_age(-5):", dog1.get_age())

