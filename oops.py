from abc import ABC, abstractmethod  # For abstraction

class Vehicle(ABC):
    def __init__(self, make, model):
        self._make = make 
        self._model = model  

    #  (Abstraction)
    @abstractmethod
    def drive(self):
        pass

    # Getter method for encapsulated attribute
    def get_make_model(self):
        return f"{self._make} {self._model}"

# Car class (Inheritance)
class Car(Vehicle):
    def __init__(self, make, model, seats):
        super().__init__(make, model)  # Inheriting attributes from Vehicle
        self.__seats = seats  # Private attribute (Encapsulation)

    #  (Polymorphism)
    def drive(self):
        print(f"Driving a {self.get_make_model()} car with {self.__seats} seats.")

# Bike class  (Inheritance)
class Bike(Vehicle):
    def __init__(self, make, model, has_gear):
        super().__init__(make, model)
        self.__has_gear = has_gear  #  (Encapsulation)

    # (Polymorphism)
    def drive(self):
        gear_status = "with gears" if self.__has_gear else "without gears"
        print(f"Riding a {self.get_make_model()} bike {gear_status}.")

# Using Polymorphism
def vehicle_drive(vehicle):
    vehicle.drive()

# Create instances
car = Car("Toyota", "Corolla", 5)
bike = Bike("Yamaha", "MT-15", True)

# Access methods
vehicle_drive(car)   # Ot: Driving a Toyota Corolla car with 5 seats.
vehicle_drive(bike)  # Ot: Riding a Yamaha MT-15 bike with gears.
