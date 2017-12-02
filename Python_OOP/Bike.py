class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price is:$" + str(self.price), "Max speed:" + str(self.max_speed) + "mph" , str(self.miles) + "miles"
        # return self
    def ride(self):
        self.miles += 10
        print "Riding" 
        # return self
    def reverse(self): 
        if self.miles >= 5:
            self.miles -= 5
        print "Reverse"
	# return self

bike1 = Bike(200,300) 
print bike1.miles
print bike1.ride
print bike1.ride
print bike1.ride
print bike1.reverse
print bike1.displayInfo()