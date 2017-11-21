class Sandwich(object):
  """A class defining a sandwich. Toppings can be added and removed, 
  and the owner and bread type can be declared upon initiation.
  
  Attributes:
    owner (str): the person puchasing the sandwich
    bread (str): the type of bread to be used
    toppings (list): a list of the toppings (str) that
      are to be put on the sandwich
    price (float): the price of the sandwich
  """
  def __init__(self, owner, bread='white'):
    """Use the sandwich constructor to initialize the owner and bread type. 
    
    Inputs:
    owner (str): the name of the knapsack's owner
    bread (str): the type of bread to be used
    
    Returns:
    A Sandwich object with no toppings
    """
    self.owner = owner
    self.bread = bread
    self.toppings = []
    
  def __add__(self, topping):
    return self.toppings.append(topping)
    
  def __sub__(self, topping):
    if topping in self.toppings:
      return self.toppings.remove(topping)
    else:
      print("Topping not present, and can't be removed.")
      
  def __eq__(self, other):
    if (self.bread==other.bread) and (sorted(self.toppings) == sorted(other.toppings)):
      return True
    else:
      return False
      
  def __ne__(self, other):
    return not (self == other)
    
  def __str__(self):
    alltops = "Toppings:\t"
    for i in self.toppings:
      alltops += " %s" % i
    return "Owner:\t\t "+ str(self.owner) +"\n" + alltops + "\nBread:\t\t " + self.bread
    
  def get_price(self, discount=0.0):
    """A function to calculate the price of the sandwich.
    Each topping costs $1, and bread that is not 'white'
    costs $2. Discounts should be applied as the amount
    to be deducted.
    
    Inputs:
      discount (float): amount to be discounted from total price
    
    Returns:
      A Sandwich object with a price attribute
    """
    self.price = 0
    for i in self.toppings:
      self.price += 1
    if self.bread != 'white':
      self.price += 2
    if discount > 0:
      self.price *= (1-discount)
    return self.price