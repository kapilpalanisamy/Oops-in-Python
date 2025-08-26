class Customer:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print("I am ",self.name,"and I am ",self.age)
c1=Customer("Kapil",20)
c2=Customer("Ram",18)
c3=Customer("Ramu",32)

l=[c1,c2,c3]

for i in l:
    i.intro()
