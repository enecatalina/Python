class Product(object):
    def __init__(self,price,item_name,weight,brand,cost,status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def price_tax(self):
        self.price * .10 
        return self
    
    def selling_status(self):
        self.status == "sold"
        return self
   
    def return_item(self,reason):
        if "defective" in reason:
            self.status = "defective"
            self.price = 0
        if "in box" in reason:
            self.status = "for sale"
        if "opened" in reason:
            self.status = "used"
            self.price * .20
        return self

    def display_all(self):
        # print "Price: {}\nName: {}\nWeight: {}\nBrand: {}\nStatus: {}".format(self.price, self.item_name, self.weight, self.brand, self.status)
        print "Price:" + str(self.price)
        print "Product:" + str(self.item_name)
        print "Weight:" + str(self.weight)
        print "Brand:" + str(self.brand)
        print "Cost:" + str(self.cost)
        print "Status:" + str(self.status)
        return self

phone1 = Product(200,"iphone",2,"apple",250,"for sale")  
phone1.display_all()