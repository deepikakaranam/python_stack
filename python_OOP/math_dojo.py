class Math_dojo:
    def __init__(self, name):
        self.name = name
        self.num = 0

    def addition(self, num1, *num):
        for n in num:
            self.num = self.num+n
        self.num = (self.num + num1)
        # print(self.num)
        return self

    def subs(self, num1, *num):
        for n in num:
            self.num = self.num-n
        self.num = (self.num-num1)
        # print(self.num)
        return self

    def result(self):
        print(self.num)
        return self


md = Math_dojo("Md")
print(md.__dict__)
md.addition(2, 3, 5).addition(2, 4, 6).subs(5, 1, 2).addition(7, 0).result()
