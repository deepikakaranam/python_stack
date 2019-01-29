class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = int(price)
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage

    def displayAll(self):
        print(
            f"price: {self.price} \n speed: {self.speed} \n fuel: {self.fuel} \n mileage: {self.mileage}")
        return self

    def Tax(self):
        if self.price > 10000:
            print("0.15")
        elif self.price < 10000:
            print("0.12")
        return self


print(Car)
acura = Car("2000", "35mph", "full", "15mpg")
second_car = Car("2000", "5mph", "Not full", "105mpg")
third_car = Car("2000", "15mph", "Kind of full", "95mpg")
fourth_car = Car("2000", "25mph", "full", "25mpg")
fifth_car = Car("2000", "45mph", "empty", "45mpg")
sixth_car = Car("20000000", "35mph", "empty", "15mpg")
print(acura.__dict__)
acura.displayAll().Tax()
second_car.displayAll().Tax()
third_car.displayAll().Tax()
fourth_car.displayAll().Tax()
fifth_car.displayAll().Tax()
sixth_car.displayAll().Tax()
