class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age   # Protected attribute (convention)
        self.__is_adult = age >= 18  # Private attribute

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Adult: {'Yes' if self.__is_adult else 'No'}")

    def have_birthday(self):
        self._age += 1
        self.__is_adult = self._age >= 18

# Creating an instance of the Person class
person1 = Person("Alice", 25)

# Accessing public attribute directly
print("Name:", person1.name)

# Accessing protected attribute (convention only)
print("Age:", person1._age)

# Trying to access private attribute directly will raise an AttributeError
# print("Is Adult:", person1.__is_adult)  # This line would raise an error.
print("Is Adult:", person1.__is_adult)