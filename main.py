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

  def Sell_item(self, name):
    index_loc = 0
    for item in self.shelf:
      index_loc += 1
      if item.name == name:
        print(index_loc)
        print(f'Before Tax: {item.price}, After Tax: {self.Apply_tax(item.price)}')
        self.shelf.pop(index_loc)
    

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
  new_inventory.Sell_item('milk')

  print(new_inventory)

