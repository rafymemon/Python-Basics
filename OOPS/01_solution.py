class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or diesel"

    @staticmethod
    def general_description():
        return "Cars are used for transport"

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


car_one = Car("Toyota", "Corrola")
# print(car_one.brand, car_one.model)

car_two = Car("Mercedez", "Mercedez benz")
# print(car_two.brand, car_two.model)

car_three = Car("suzuki", "Mehran")
# print(car_three.full_name())

safari = Car("Tata", "Safari")
# print(safari.fuel_type())

my_tesla = ElectricCar("tesla", "tesla s", "85kwh")
print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.fuel_type())

# print("Total Cars :", Car.total_car)
# print(car_two.general_description())


my_car = Car("tata", "safari")
print(isinstance(my_car, ElectricCar))

# my_car.model = "corrola"
# print(my_car.model())


class Battery:
    def batteryInfo(self):
        return "This is a battery"


class Engine:
    def EngineInfo(self):
        return "This is a Engine of a Car"


class ElectricCar_two(Battery, Engine, Car):
    pass  # Pass is special keyword used as a placeholder for a code. In python when we make a class and we want to specify the use case later we just use pass to avoid error and code still being empty


my_tesla_car = ElectricCar_two("tesla", "Model S")
print(my_tesla_car.batteryInfo())
print(my_tesla_car.EngineInfo())
