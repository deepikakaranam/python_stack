class Product:
    def __init__(self, price, weight, Brand):
        self.price = int(price)
        self.weight = float(weight)
        self.Brand = Brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        print(self.status)
        return self

    def AddTax(self, tax):
        sales_tax = (self.price*0.12)
        self.price = (self.price)-sales_tax
        print(self.price)
        return self

    def Return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            print(self.status)
            self.price = 0
            print(f"price is {self.price}")

        if reason_for_return == "like_new":
            self.status = "for sale"
            print(self.status)
        elif reason_for_return == "opened":
            self.status = "used"
            print(self.status)
            self.price = self.price-(self.price*0.02)
            print(self.price)
        return self

    def displayInfo(self):
        print(self.price, self.weight, self.Brand, self.status)
        return self


laptop = Product("600", "300", "Asus")
print(laptop.__dict__)
laptop.sell().AddTax(0.12).Return_item("opened").displayInfo()
