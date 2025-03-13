# You have been tasked with parsing menus from a large restaurant group. Each menu is streamed to clients via a provided interface. You must design object(s) that represents a menu and can be instantiated with data from the provided interface. Your design should contain an appropriate class structure to contain the parsed data, as well as a function or set of functions to perform the parsing.
"""


"""

# Consumers will use your object(s) to access a complete representation of the data sent by the menu stream after it has finished loading. Your objects should provide easy access to the full representation of the menu. It should be possible to reconstruct the menu stream from your object.

# The menu stream represents a list of menu items. Each line in the stream is a property of a menu item, and each item will be separated by an empty string. The attributes of each item are as follows:

#   Line 0: The ID of the item
#   Line 1: The item type, either CATEGORY, DISH or OPTION
#   Line 2: The name of the item
#   Line 3: The price of the item for DISH and OPTION. Not present for CATEGORY items.
#   Any other line: A list of item IDs that are linked to the current item. OPTIONs do not have any linked items.

# 4
# DISH
# Spaghetti
# 10.95
# 2
# 3

# 1
# CATEGORY
# Pasta
# 4
# 5

# 2
# OPTION
# Meatballs
# 1.00

# 3
# OPTION
# Chicken
# 2.00

# 5
# DISH
# Lasagna
# 12.00

#  be separated by an empty string.
# 6
# DISH
# Caesar Salad
# 9.75
# 3

#print(input)
# 4.  <
# DISH
# Spaghetti
# 10.95
# 2
# 3
# ''
# 1
# CATEGORY
# Pasta
# 4
# 5
import unittest
from abc import ABC, abstractmethod
from typing import Optional, List
class MenuStream(ABC):
    #Iterator
    @abstractmethod
    def next_line(self) -> str:
        pass 


class MenuStreamImplementation(MenuStream):
    def __init__(self):
        self._stream = ['4', 'DISH', 'Spaghetti', '10.95', '2', '3', '', '1', 'CATEGORY', 'Pasta', '4', '5', '', '2', 'OPTION', 'Meatballs', '1.00', '', '3', 'OPTION', 'Chicken', '2.00', '', '5', 'DISH', 'Lasagna', '12.00', '', '6', 'DISH', 'Caesar Salad', '9.75', '3', '']
    
    def next_line(self):
        return self._stream.pop(0) if self._stream else None


class Item():
    def __init__(self, id, type_item, name, price: Optional[float] = None, linked_items: Optional[list[str]] = None) -> None:
        self.id = id
        self.type = type_item
        self.name = name
        self.price = price
        self.linked_items = linked_items

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.id == other.id and self.type == other.type and self.name == other.name and self.price == other.price and self.linked_items == other.linked_items
        return False
    
    def __hash__(self):
        return hash((self.id, self.type, self.name, self.price, tuple(self.linked_items) if self.linked_items else None))
    
    def __str__(self):
        return(f"Item: {self.id}\n"
            f"Type: {self.type}\n"
            f"Name: {self.name}\n"
            f"Price: {self.price}\n"
            f"Linked_items: {self.linked_items}\n")


def parse_menu(menu_stream) -> List[Item]:
    items = []
    input_items = menu_stream.next_line()
    while input_items:
        stream = []
        while input_items:
            #print(input_items)
            stream.append(input_items)
            input_items = menu.next_line()
        id = stream[0]
        item_type = stream[1]
        name = stream[2]

        if item_type == 'CATEGORY':
            linked_items = stream[3:]
            category_item = Item(id, item_type, name, None, linked_items)
            items.append(category_item)
        elif item_type == 'DISH':
            price = float(stream[3])
            linked_items = stream[4:]
            category_dish= Item(id, item_type, name, price, linked_items)
            items.append(category_dish)
        elif item_type == 'OPTION':
            price = float(stream[3])
            category_option = Item(id, item_type, name, price, None)
            items.append(category_option)
        input_items = menu.next_line()
    return items

menu = MenuStreamImplementation()
items = parse_menu(menu)
for item in items:
    print(item)
    
spaghetti = Item('4', 'DISH', 'Spaghetti', 10.95, ['2', '3'])
assert spaghetti in items, "Spaghetti dish should be in the items list"

pasta = Item('1', 'CATEGORY', 'Pasta', None, ['4', '5'])
assert pasta in items, "Pasta category should be in the items list"

meatballs = Item('2', 'OPTION', 'Meatballs', 1.00, None)
assert meatballs in items, "Meatballs option should be in the items list"

chicken = Item('3', 'OPTION', 'Chicken', 2.00, None)
assert chicken in items, "Chicken option should be in the items list"

lasagna = Item('5', 'DISH', 'Lasagna', 12.00, [])
assert lasagna in items, "Lasagna dish should be in the items list"

caesar_salad = Item('6', 'DISH', 'Caesar Salad', 9.75, ['3'])
assert caesar_salad in items, "Caesar Salad dish should be in the items list"

print("All assertions passed.")
#print(items)





        

    





