class car:
    def __init__(self,Name,Manufacturer,model,color):
        self.Name=Name
        self.Manufacturer=Manufacturer
        self.model=model
        self.color=color
    def accelerate(self):
        print("The color of the car is : ",self.color)
    def stop(self):
        print("The Manufacturer of the car is ",self.Manufacturer)
        print("The model of the car is ",self.model)

car1=car("Zen","Maruti","1990","Red")
car1.accelerate()
car2=car("800","Maruti","1995","Grey")
car2.stop()
car3=car("Verna","Hyundai","2006","Blue")
car3.stop()