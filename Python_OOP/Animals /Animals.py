
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

dog = Animals("Bella",30)
dog.walk().walk().walk().run().run()
dog.display_health()



