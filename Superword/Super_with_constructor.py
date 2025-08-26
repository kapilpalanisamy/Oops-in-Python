################ Super Example with constructor ################

class Phone:
    def __init__(self, price, brand, camera):
        
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        
        print("before")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")

# Object creation
s = SmartPhone(20000, "Samsung", 12, "Android", 2)

# Accessing attributes
print(s.os)
print(s.brand)
