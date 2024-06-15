import ecommerce.shipping
ecommerce.shipping.cal_shipping()

import random

for i in range(3) :
  print(random.random())
  print(random.randint(10, 20))


members = ["HASHIM ", "BAYA", "NASSORO"]
leader = random.choice(members)
print(leader)

class Dice :
  def roll(self) :
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    return (first, second)
  

dice = Dice()
print(dice.roll())

from pathlib import Path 

path = Path("ecommerce")
print(path.exsts())
  
