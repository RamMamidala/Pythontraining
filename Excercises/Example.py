class vehicle:
    def __init__(self,color,seater):
        self.color=color
        self.seater=seater
    def car(self):
        print("No.of seats are "+str(self.seater))
    def bike(self):
        print("No.of seats are "+str(self.seater))

class NewVehicle(vehicle):
    def __init__(self,size,price):
        self.size=size
        self.price=price
    def  car(self):
        print("Price of the car is "+str(self.price))    


obj1=vehicle("Red",4)
obj1.car()

                    