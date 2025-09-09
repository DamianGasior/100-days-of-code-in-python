# Create a base class Vehicle with attributes:
# brand
# model
# and a method info() that returns the text "Vehicle: brand model".

# Create two derived classes:
# Car – add an attribute seats (number of seats).
# Bike – add an attribute type (e.g., "mountain", "road").

# In both classes, use super() in the constructor to call the base class __init__.
# Override the info() method in each class to return a more detailed description:

# Car: "Car: brand model, number of seats: seats"

# Bike: "Bike: brand model, type: type"

# Create a list vehicles containing several Car and Bike objects, represent the list in a seperate class

# Iterate over the list and call the info() method for each object → this will demonstrate polymorphism.

class Fleet:

    def __init__(self):
        self.list_of_vehicles = []

    def add_vehiclet(self, type_of_vehicle):
        if isinstance(type_of_vehicle,Vehicle):
            self.list_of_vehicles.append(type_of_vehicle)
        else:
            raise ValueError ('object is not a Vehicle type')

    def info_from_list(self):
        return [v.info() for v in self.list_of_vehicles]


class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Vehicle : {self.brand} , model: {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, seats=4):
        super().__init__(brand, model)
        self.seats = seats

    def info(self):
        return f"Car: brand:{self.brand}, model:{self.model}, number of seats :{self.seats}"


class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def info(self):
        return f"Bike: brand:{self.brand}, model:{self.model}, type :{self.bike_type}"


normal_car = Vehicle("auto", "personal car")
specific_car = Car("Fiat", "Uno")
specific_car2 = Car("Opel", "Kadett")

specific_bike = Bike("Romet", "alfa", "normal")
specific_bike2 = Bike("Gazelle", "beta", "speed bike")


print(normal_car.info())

list1 = Fleet()

list1.add_vehiclet(specific_car)
list1.add_vehiclet(specific_car2)
list1.add_vehiclet(specific_bike)
list1.add_vehiclet(specific_bike2)


print(list1.info_from_list())