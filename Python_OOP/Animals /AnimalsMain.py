class Animals(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "{}'s health is {}".format(self.name, self.health)
        return self

class Dog(Animals):
    def __init__(self, name,health):
        super(Dog,self).__init__(name,health)
        self.health = 150

    def pet(self):
        self.health =+ 5
        return self

class Dragon(Animals):
    def __init__(self,name,health):
        super(Dragon,self).__init__(name,health)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

dog = Animals("Bella",30)
dog.walk().walk().walk().run().run()
dog.display_health()

dragon = Dragon("JohnSnow",170)
dragon.fly()
dragon.display_health()    

    

