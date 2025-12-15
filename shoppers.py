"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #1 (25 points)
Filename: shoppers.py

An item has an item code (e.g. "ABCD-1234"), a name (e.g. "Silky Camisole"), 
and a price (e.g. $24). 
A partially completed item class has been provided to you below. You must 
complete the class by making the following enhancements:
- Write accessors for all fields.
- Two items are considered equal if they have the same item code.
- Items should be capable of being used with hashing data structures.
- The string representation of an item is its its code, name, and price
  seperated by commmas in a parenthesis, e.g. "(ABCD-1234, Silky Camisole, 24)"
- Items can be sorted based on the item code.
Write down the manual test by creating at least two items.
"""

class Item:
    __slots__ = ["__item_code", "__name", "__price"]

    def __init__(self, item_code, name, price):
      self.__item_code = item_code
      self.__name = name
      self.__price = price

    def __eq__(self, value):
      if type(self) == type(value):
        if self.__item_code == value.__item_code:
            return True
      return False
    
    def __hash__(self):
      return hash(self.__item_code)
    
    def __repr__(self):
      return "(" + str(self.__item_code) + ", " + self.__name + ", " + str(self.__price) + ")"
    
    def get_code(self):
      return self.__item_code
    
    def get_name(self):
      return self.__name

    def get_price(self):
      return self.__price

def item_key(item):
  return item.get_code()

# manual test from main() method
def main():
  item1 = Item("ABC-123", "Silky Camisole", 24)
  item2 = Item("ZXC-098", "Food", 10)
  list1 = [item2,item1]

  print(item1, item2, sep="\n")
  print(item1 == item2)
  print(item1 == 2)
  print(set(list1))

  list1.sort(key=item_key)
  print(list1)

if __name__ == "__main__":    main()