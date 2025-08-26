#inheriting the private members of the parent class = not possible
class Phone:

    def __init__(self,price,brand,camera):
        print("inside the phoen constructor")
        self.price=price
        self.__brand=brand
        self.camera = camera

class Smartphone(Phone):
    pass

s=Smartphone(20000,'apple',13)
print(s.__brand)
