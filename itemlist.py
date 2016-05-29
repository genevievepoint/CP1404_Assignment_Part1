# Genevieve Point
from A2 import load_items

# filename = 'items.csv'
# list_of_items = load_items(filename)
# print(list_of_items)
#
class ItemList:

    def __init__(self, list):
        self.items_list = list

    def get_items(self, logical_position):

        item = self.items_list[logical_position]
        return item

    def get_list_length(self):

        length_of_list = len(self.items_list)
        return length_of_list

    def find_item_logical_position(self, name):

        reference = -1
        counter = 0
        for item in self.items_list:
            if item.name == name:
                reference = counter
                if reference > -1:
                    return reference

            counter += 1

        return False + reference

    def return_all(self):
        return self.items_list

    def add_new_item(self, new_item_object):
        self.items_list.append(new_item_object)



#