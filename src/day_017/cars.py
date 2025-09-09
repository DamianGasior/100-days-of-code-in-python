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

# Create a list vehicles containing several Car and Bike objects.

# Iterate over the list and call the info() method for each object → this will demonstrate polymorphism.


class Vehicle:

    list_of_vehicles = []

    @classmethod
    def add_vehiclet(cls, type_of_vehicle):
        cls.list_of_vehicles.append(type_of_vehicle)

    @classmethod
    def info_from_list(cls):
        for i in cls.list_of_vehicles:
            print(i)

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
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def info(self):
        return f"Bike: brand:{self.brand}, model:{self.model}, type :{self.type}"


normal_car = Vehicle("auto", "osobowe")
specific_car = Car("Fiat", "Uno")
specific_car2 = Car("Opel", "KAdett")

specific_bike = Bike("Romet", "alfa", "normaln")
specific_bike2 = Bike("Gassele", "beta", "speed bike")


print(normal_car.info())

Vehicle.add_vehiclet(specific_car)
Vehicle.add_vehiclet(specific_car2)
Vehicle.add_vehiclet(specific_bike)
Vehicle.add_vehiclet(specific_bike2)

for veh in Vehicle.list_of_vehicles:
    print(veh.info())
