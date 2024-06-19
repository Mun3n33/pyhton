# Encapsulation
class Car:
    def __init__(self, brand, size, model, manufacturersdetails):
        self.brand = brand
        self.size = size
        self.model = model
        self.__manufacturersdetails = manufacturersdetails

    def display(self):
        print(f'Brand: {self.brand}')
        print(f'Size: {self.size}')
        print(f'Model: {self.model}')
        print(f'Manufacturers details: {self.__manufacturersdetails}')


car1 = Car('BMW', 'Large SUV', 'M13', 'Ad4F*OP')

print("This car is of", car1.brand, "brand", "it a", car1.size, "model", car1.model)
# public properties

# private
# print("Manufacturer's Details", car1.__manufacturersdetails)
# Trying to access private attribute directly will raise an AttributeError
# unless one uses a getter method
