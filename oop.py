class Kettle(object):
    
    power_source = "electricity"
    
    def __init__(self, make, price):
        self.make=make
        self.price=price
        self.on= False
        
    def switch_on(self):
        self.on = True

Kenwood = Kettle("Kenwood", 42.99)
print(Kenwood.make)
print(Kenwood.price)

Kenwood.price= 12.75
print(Kenwood.price)

Hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(Kenwood.make, Kenwood.price, Hamilton.make, Hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(Kenwood, Hamilton))

print("*" * 80)

print(Hamilton.on)
Hamilton.switch_on()
print(Hamilton.on)

Kettle.switch_on(Kenwood)
print(Kenwood.on)

print("*" * 80)

Kenwood.power= 1.5
print(Kenwood.power)

print("Switch to atomic power")
Kettle.power_source= "atomic"

print(Kettle.power_source)
print(Kenwood.power_source)
print(Hamilton.power_source)

print("*" * 80)
print(Kettle.__dict__)
print(Kenwood.__dict__)
print(Hamilton.__dict__)

print(Kettle.__module__)
print(Kettle.__weakrefoffset__)
print(Kettle.__doc__)

