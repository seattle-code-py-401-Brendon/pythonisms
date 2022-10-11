class Item:
  def __init__(self, name, price=0, total=0):
    self.name = name
    self.price = price
    self.total = total

  def __repr__(self):
        return f'{self.name}:{self.price}'


class Inventory:
  def __init__(self, shelf = [], total_inventory_cost = 0):
    self.shelf = shelf
    self.total_inventory_cost = total_inventory_cost

  def Stock_item(self, name, price):
    new_item = Item(name,price)
    self.shelf.append(new_item)

  # ethod is dependant on another method to apply tax
  def Sell_item(self, name, apply_tax):
    index_loc = 0
    for item in self.shelf:
      index_loc += 1
      if item.name == name and apply_tax is True:
        print(f'Before Tax: {item.price}, After Tax: {self.Apply_tax(item.price)}')
        self.shelf.pop(index_loc -1)
        return
      elif apply_tax is False:
        print(f'Item Price: {item.price}')
        return self.shelf.pop(index_loc -1)
    print('item unavailable')
      
    
# decorator function to apply tax
  def Apply_tax(self, price):
    return price + price * .08
  
  def __repr__(self):
       return f'{self.shelf}'
  

if __name__ == '__main__':

  
  new_inventory = Inventory()
  new_inventory.Stock_item('apple', 10.99)
  new_inventory.Stock_item('banana', 9.99)
  new_inventory.Stock_item('pineapple', 4.99)
  new_inventory.Stock_item('milk', 4.99)
  
  # you can apply tax or not with boolean
  new_inventory.Sell_item('banana', True)

# prints out the inventory of as initial. 
  print(new_inventory)

