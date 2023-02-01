class Mammal(object):
  neo_cortex = True
 
class Cat(Mammal):
  def __init__(self, name, years):
    self.name = name
    self.years = years
 
  def eat(self, food):
    print(f'nom {food}')
 
fry_cat = Cat('Fry', 7)
fry_cat.eat('steak')

def print_hi(name, *args):
  # Use a breakpoint in the code line below to debug your script.
  print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
  for index, arg in enumerate(args):
    print(index, arg)

print_hi('hello', 'a', 'b')