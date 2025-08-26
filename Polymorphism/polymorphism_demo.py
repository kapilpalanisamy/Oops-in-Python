#polymorphism and the method overriding
class Phone:

    def __init__(self,price,brand,camera):
        print("inside the phone constructor")
        self.price=price
        self.brand=brand
        self.camera = camera
        
    def buy(self):
        print("Buying a phone")

class Smartphone(Phone):

    def buy(self):
        print("buying a smartphone")

s=Smartphone(20000,'apple',13)

s.buy()
