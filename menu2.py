# You have been tasked with parsing menus from a large restaurant group. Each menu is streamed to clients via a provided interface. You must design object(s) that represents a menu and can be instantiated with data from the provided interface. Your design should contain an appropriate class structure to contain the parsed data, as well as a function or set of functions to perform the parsing.

# Consumers will use your object(s) to access a complete representation of the data sent by the menu stream after it has finished loading. Your objects should provide easy access to the full representation of the menu. It should be possible to reconstruct the menu stream from your object.

# The menu stream represents a list of menu items. Each line in the stream is a property of a menu item, and each item will be separated by an empty string. The attributes of each item are as follows


# Line 0: The ID of the item
# Line 1: The item type, either CATEGORY, DISH or OPTION
# Line 2: The name of the item
# Line 3: The price of the item for DISH and OPTION. Not present for CATEGORY items.
# Any other line: A list of item IDs that are linked to the current item. OPTIONs do not have any linked items.

# Sample Menu:

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

# 6
# DISH
# Caesar Salad
# 9.75
# 3



from abc import ABC, abstractmethod

class MenuStream(ABC):
    @abstractmethod
    def next_line(self) -> str:
        pass 


class MenuStreamImplementation(MenuStream):
    def __init__(self):
        self._stream = ['4', 'DISH', 'Spaghetti', '10.95', '2', '3', '', 
        '1', 'CATEGORY', 'Pasta', '4', '5', '', 
        '2', 'OPTION', 'Meatballs', '1.00', '', 
        '3', 'OPTION', 'Chicken', '2.00', '', 
        '5', 'DISH', 'Lasagna', '12.00', '', 
        '6', 'DISH', 'Caesar Salad', '9.75', '3', '']
    
    def next_line(self):
        return self._stream.pop(0) if self._stream else None


class Item(ABC):

    def __init__(self, id, item_type, name, price, item_list):
        self.id= id,
        self.type= item_type,
        self.name= name,
        self.price= price,
        self.item_list= item_list
        self.items = []
    
    def __str__(self) -> str:
        return f"id: {self.id} type: {self.type}, name: {self.name}, price: {self.price}, item_list: {self.item_list}"


"""
    item_type,
    name,
    price,
    items_linked
"""

#MenuStreamImplementation



class MenuParser():
    
    def __init__(self, menu_imple):
        self.MenuImplementation = menu_imple
        self.dict_items = {}


    def parse(self, menu_css):
        while True:
            id_item = self.MenuImplementation.next_line()
            if id_item:
                item_type = self.MenuImplementation.next_line()
                item_name = self.MenuImplementation.next_line()
                if item_type == 'CATEGORY':
                    item_price = None
                else:
                    item_price = self.MenuImplementation.next_line()
                item_list=[]
                while True:
                    item_id = self.MenuImplementation.next_line()
                    if item_id:
                        item_list.append(item_id)
                    else:
                        break
                    
                menu_item = Item(id_item, item_type, item_name, item_price, item_list)
                self.dict_items[id_item] = menu_item
                print(menu_item)
                menu_css.append(menu_item)
            else:
                break

    def populate_items(self, menu_css):
        for menu_item in menu_css:
            if menu_item.item_list:
                item_elem = self.dict_items[menu_item]
                menu_item.items.append(item_elem)




        #print(self.MenuImplementation.next_line())


menu_imple = MenuStreamImplementation()

menu_parser = MenuParser(menu_imple)
menu_css = []
menu_parser.parse(menu_css)

print(menu_css)















