class Person():
    def __init__ (self, name, age, adress):
        self.namn = name
        self.adress = adress
        self.ålder = age

    def presentMyself(self):
        print("Hello my name is", self.namn)

    def increaseAge(self):
        self.ålder += 1

    def getAge(self):
        return self.ålder