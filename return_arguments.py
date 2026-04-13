class random():
    def __init__(self,num,name):
        self.num=num
        self.name=name

    def vehicle(self):
        return f"My vehicle name is {self.name} and it's register number: {self.num}"

v1=random(1735,'RoyalEnfield')
x=v1.vehicle()
print("SUCCESSFULLY COMPLETED")
