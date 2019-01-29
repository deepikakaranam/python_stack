class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        print(self.health)
        return self

    def run(self):
        self.health -= 5
        print(self.health)
        return self

    def display_health(self):
        print(self.health)
        return self


cat = Animal("Cat")
print(cat.__dict__)
cat.walk().walk().walk().run().run().display_health()


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        print(self.health)
        return self


brownie = Dog("Brownie")
print(brownie.__dict__)
brownie.walk().walk().walk().run().run().pet().display_health()
# brownie.fly()


class Dragon(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        print(self.health)
        return self

    def display_health(self):
        super().display_health()
        print("Iam a Dragon")


pete = Dragon("pete")
print(pete.__dict__)
pete.display_health()


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200


willie = Elephant("willie")
print(willie.__dict__)
# willie.fly()
willie.display_health()
