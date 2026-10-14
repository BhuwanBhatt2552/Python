# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class vehicle:
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle

  def drive(self, speed):
    self.mode = "Driving"
    self.speed = speed  



    pass

class Car(vehicle):
  def __init__(self, engine):
    super().__init__("CAR")
    self.wheels = 4
    self.doors = 4
    self.engine = engine

  def drive(self, speed):
    super().drive(speed)
    print("Driving my", self.engine, "car at", self.speed)

    
class motorcycle(vehicle):
  def __init__(self, engine, sidecar):
    super().__init__("Motorcycle")

    if (sidecar):
      self.wheels = 3
    else:
      self.wheels = 2

    self.doors = 0
    self.engine = engine
  def drive(self, speed):
      super().drive(speed)
      print("Driving my", self.engine, "motorcylce at", self.speed)   

car1 = Car("petrol")
car2 = Car("electric")
car1.drive(80)
car2.drive(100)
mc1 = motorcycle("petrol", True)
mc1.drive(50)
print(mc1.wheels)
print(car1.engine)
print(car2.doors)
