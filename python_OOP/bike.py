class Bike:
    def __init__(self, price):
        self.price = 100
        self.max_speed = 25
        self.miles = 0

    def displayInfo(self):
        print(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        print("Riding")
        self.miles += 10
        print(self.miles)
        return self

    def reverse(self):
        print("Reversing")
        if self.miles > 0:
            self.miles -= 5
        else:
            self.miles = 0

        print(self.miles)
        return self


new = Bike("New")
apache = Bike("Apache")
victor = Bike("Victor")
print(new)
print(apache)
print(new.__dict__)
print(new.price)
print(new.max_speed)
new.displayInfo()
new.ride()
new.reverse()
new.ride().ride().ride().reverse().displayInfo()
apache.ride().ride().reverse().reverse().displayInfo()
victor.reverse().reverse().reverse().displayInfo()
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

# What would you do to prevent the instance from having negative miles?

# Which methods can return self in order to allow chaining methods?
