class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} barks!"

# Create two Dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Poodle")

# Access attributes and call methods
print(dog1.name)    # Output: Buddy
print(dog2.bark())  # Output: Max barks!