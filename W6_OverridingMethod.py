class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details : ', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')

# Inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def charge_gear(self):
        print('Car change 7 gear')

# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# Calls method from car class
car.max_speed()
car.change_gear()

#Vehicle object
vehicle = Vehicle('Truck x1', 'White', 75000)
vehicle.show()

# Calls method from a vehicle class
vehicle.max_speed()
vehicle.change_gear()