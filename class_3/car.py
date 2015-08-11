class Vehicle(object):

    @classmethod
    def print_number_of_wheels(cls):
        print(cls.WHEELS)


class Car(Vehicle):
    WHEELS = 4

    def __init__(self, model, brand, position=0):
        self.model = model
        self.brand = brand
        self.position = position

    def move(self):
        self.position += 1


class Bike(Vehicle):
    WHEELS = 2


Car.print_number_of_wheels()

Car.WHEELS = 7

Car.print_number_of_wheels()

"""
gt = Car("Ford", "GT")


print "GT has {} wheels".format(gt.WHEELS)

focus = Car("Ford", "Focus")
focus.model  # Focus

print "Focus has {} wheels".format(focus.WHEELS)

print "Car class has {} wheels".format(Car.WHEELS)

Car.WHEELS = 5


print "Again, Car class has {} wheels".format(Car.WHEELS)

print "Finally, Focus has {} wheels".format(focus.WHEELS)
"""