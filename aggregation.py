class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address

    def editprofile(self,newname,newcity,newpin,newstate):
        self.name=newname
        self.address.change_address(newcity,newpin,newstate)

class Address:

    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state

        
    def change_address(self,newcity,newpin,newstate):
        self.city=newcity
        self.pincode=newpin
        self.state=newstate

add=Address("Banglore",562112,"karanatka")
cust=Customer("kapil","Male",add)

cust.editprofile("Ankit","gurugaon",122011,"haryana")

print(cust.address.pincode)
