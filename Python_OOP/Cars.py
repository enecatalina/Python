class Car(object):
    def __init__(self,price, speed, fuel, mileage):
        print "Time to buy a car!!!"
        self.price = price
        if 
        self.speed = speed 
        self.fuel = fuel 
        self.mileage = mileage
        self.tax = 0
        if price > 10000:
            self.tax = 15
        else: 
            self.tax = 12
        self.display_all()

    def display_all(self):
        print "Price:$" + str(self.price) 
        print "Speed:" + str(self.speed) + "mph"
        print "zfuel:" + str(self.fuel)
        print "Mileage:" + str(self.mileage) + "miles"
        print "Tax:" + str(self.tax) + "%"
 
car1 = Car(11000,50,"full",500,)
car2 = Car(5000,60,"half full", 1000)
car3 = Car(15000,100,"empty",10)
car4 = Car(5000,80,"full",400)
car5 = Car(20000,50,"quater full",200)
car6 = Car(6000,70,"empty",500)