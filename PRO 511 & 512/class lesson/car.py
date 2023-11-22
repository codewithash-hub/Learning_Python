# create a class
class Car:
    # Initialize attributes.
    def __init__(self, name, model):
        # Make attributes accessible to the whole program.
        self.name = name
        self.__model = model
        
    # method a car to perfom.
    def race(self):
        return f"{self.name} {self.__model} is a racing car"

# define an object.
obj_toyota = Car('Mercdes Benz', 'CLA 250 AMG Line')

# print the function/method of a car using a dot notation.
print(obj_toyota.race())


