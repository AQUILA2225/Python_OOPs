class User:
    def __init__(self, n, loc):
        self.name= n
        self.location=loc
    
    def login(self):
        print(self.name, "logged in from location", self.location)

class Customer(User):
    def __init__(self,n, loc, order_item):
        super().__init__(n,loc)
        self.order_item=order_item 
    
    def place_order(self):
        print(self.name, "Ordered", self.order_item)

class DeliveryPartner(User):
    def __init__(self, n, loc, vehicle_type):
        super().__init__(n,loc)
        self.vehicle_type = vehicle_type
    
    def deliver_order(self):
        print(self.name, "is delivering using", self.vehicle_type)

cus = Customer("Bharathi", "Hyderabad", "Veg Biriyani")
dp = DeliveryPartner("Ravi", "Hyderabad", "Bike")

cus.login()
cus.place_order()

dp.login()
dp.deliver_order()




