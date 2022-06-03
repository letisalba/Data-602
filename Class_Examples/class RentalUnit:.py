class RentalUnit:
  x = 0

u1 = RentalUnit()
u1.x = 5
print(u1.x)

u2 = RentalUnit()
print(u2.x)

------------------------------------------------------
class RentalUnit:
  y = 10
  x = 3 * y
  def __init__(self,x,y):
    self.x = x
    self.y = y


u1 = RentalUnit(100,200)
u1.x = 5
print(u1.x)

u2 = RentalUnit(500,800)
print(u2.x)

------------------------------------------------------
class RentalUnit:
  def __init__(self,r): # constructor
    self.rent = r # the idea 'self'
  def print_rent(self):
    print(self.rent)
  def calc_annual(self):
    print(12*self.rent)
u1 = RentalUnit(1000)
u2 = RentalUnit(5000)
u3 = RentalUnit(7200)
u1.calc_annual()

-----------------------------------------------------
import replit,time
class Box:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def shift(self,shift):
    self.shift = shift
    for s in range(shift):
      for n in range(self.y):
        spaces = ' ' * s
        asterisks = '*' * self.x
        print(spaces + asterisks)
      time.sleep(1)
      replit.clear()
  def rotate():
    a = self.x
    self.x = self.y
    self.y = a

b = Box(10,5)
b.shift(10)
b.rotate()
b.shift(10)