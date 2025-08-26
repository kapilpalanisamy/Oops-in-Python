# Multiple Inheritance Example

class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price   # private attribute
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class Product:
    def review(self):
        print("Customer review")


class SmartPhone(Phone, Product):   # Inheriting from both Phone and Product
    pass


# Object creation
s = SmartPhone(20000, "Apple", 12)
s.buy()       # from Phone
s.review()    # from Product
