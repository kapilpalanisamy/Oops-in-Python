class Parent:
    
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

class Child(Parent):
    
    def __init__(self, num, val):
        
        super().__init__(num)
        self.__val = val

    def get_val(self):
        return self.__val

son = Child(100, 200)
print(son.get_num())
print(son.get_val())

'''
class Parent:
    def __init__(self):
        self.num = 100

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 200

    def show(self):
        print(self.num)
        print(self.var)

son = Child()
son.show()
'''
