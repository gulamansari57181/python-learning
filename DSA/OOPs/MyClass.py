# Creating a class and object with default constructor

class Car:
    # By default comstructor in python
    def __init__(self,brand,color):
        self.brand=brand
        self.car=color
        print(f"Car's brand is {brand}")
        print(f"Car's color is {color}")

# Creating object of class Car

car1 = Car("BMW","Black")
car2 = Car("Audi","Silver")