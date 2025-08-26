#pass by reference
class Customer:

    def __init__(self,name):
        self.name=name

def greet(customer):
   print(id(customer))
   customer.name="kapil"
   print(customer.name)
   print(id(customer))
   
cust=Customer("Nithish")

print(id(cust))

greet(cust)

print(cust.name)

#class ke object are also mutable like lists , dictionaries and sets .
