class Geometry:

    '''def area(self,radius):
        return 3.14*radius*radius

    def area(self,l,b):
        return l*b'''

    def area(self,a,b=0):
        if b==0:
            print("circle",3.14*a*a)
        else:
            print("rectange",a*b)

obj=Geometry()
print(obj.area(4))
print(obj.area(4,5))
