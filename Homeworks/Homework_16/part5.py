

class Car:
    total_cars = 0

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return f"Total cars: {cls.total_cars}"


c1 = Car("BMW")
c2 = Car("Mercedes")
c3 = Car("Toyota")

print(Car.get_total_cars())




























