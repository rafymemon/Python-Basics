class Car:
    def __init__(self, brand, model):
        self.__brand = brand # __brand shows that the attribute is private and can only be accessible inside the class
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

    def get_brand(self):
        return self.__brand + " !"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("tesla", "tesla s", "85kwh")
print(my_tesla.get_brand(), my_tesla.model, my_tesla.battery_size)

my_car = Car("toyota", "Corrola")
print(my_car.get_brand(), my_car.model)
