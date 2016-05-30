from kivy.app import App
from kivy.lang import Builder
# from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import StringProperty
from A2 import load_items
from itemlist import *
from item import *

filename = 'items.csv'
list_of_items = load_items(filename)
print(list_of_items)
list_of_Item_objects = []
for i in range(0, len(list_of_items), 1):
    new_item = list_of_items[i]
    new_item_name = new_item[0]
    new_item_description = new_item[1]
    new_item_price = new_item[2]
    new_item_status = new_item[3]
    New_Item_object = Item(new_item_name, new_item_description, new_item_price, new_item_status)
    # print(New_Item_object)
    list_of_Item_objects.append(New_Item_object)

# Test_list = ItemList(list_of_Item_objects)
# test_item = Item("Game", "Board Game", "3.14", "in")
# Test_list.add_new_item(test_item)
# print(Test_list.get_list_length())
# print(Test_list.find_item_logical_position("Game"))
# print(Test_list.get_items(Test_list.find_item_logical_position("Game")))
TOTAL_HIRE_PRICE = ''
HIRE_ITEM_LIST = []
RETURN_ITEM_LIST = []

# The custom App class
class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.items = ItemList(list_of_Item_objects)
        self.status_text = ''
        self.running_mode = 'list'

# Creates the window and provides the basic information used in the start up of the program
    def build(self):
        self.title = "EquipmentHire"
        self.root = Builder.load_file('gui.kv')
        self.create_entry_buttons()
        return self.root

    def create_entry_buttons(self):
        for items in self.items.return_all():
            temp_button = Button(text=items.name)
            temp_button.bind(on_release=self.press_entry)
            if items.status == 'in':
                temp_button.background_color = (0, 0, 1, 1)
            elif items.status == 'out':
                temp_button.background_color = (0, 1, 0, 1)
            self.root.ids.items_grid.add_widget(temp_button)

    def press_entry(self, instance):
        if self.running_mode == 'list':
            current_item = instance.text
            current_item_position = self.items.find_item_logical_position(current_item)
            current_item_object = self.items.get_items(current_item_position)
            current_item_name = current_item_object.name
            current_item_description = current_item_object.description
            current_item_price = current_item_object.price
            current_item_status = current_item_object.status
            self.root.ids.status_text.text = "{} {} {} {}".format(current_item_name, current_item_description,
                                                                  current_item_price, current_item_status)
        elif self.running_mode == 'hire':
            current_item = instance.text
            current_item_position = self.items.find_item_logical_position(current_item)
            current_item_object = self.items.get_items(current_item_position)
            if current_item_object.status == 'in':
                current_item_position = self.items.find_item_logical_position(current_item)
                current_item_object = self.items.get_items(current_item_position)
                current_item_name = current_item_object.name
                current_item_description = current_item_object.description
                current_item_price = current_item_object.price
                current_item_status = current_item_object.status
                self.root.ids.status_text.text = "Hiring:{} {} {} {}".format(current_item_name, current_item_description
                                                                             , current_item_price)

        elif self.running_mode == 'return':
            current_item = instance.text
            current_item_position = self.items.find_item_logical_position(current_item)
            current_item_object = self.items.get_items(current_item_position)
            if current_item_object.status == 'out':
                current_item_position = self.items.find_item_logical_position(current_item)
                current_item_object = self.items.get_items(current_item_position)
                current_item_name = current_item_object.name
                current_item_description = current_item_object.description
                current_item_price = current_item_object.price
                current_item_status = current_item_object.status
                self.root.ids.status_text.text = "Returning: {}".format(current_item_name)

        instance.state = 'down'
        # instance.state = 'normal'

    def press_add(self):
        """
        this opens the popup for creating a new item entry
        """
        # self.status_text = "Enter details for new item"
        self.root.ids.popup.open()

    def press_save_new_item(self, new_item_name, new_item_description, new_item_price):
        error_marker = 0
        try:
            check_price = float(new_item_price)

        except ValueError:
            error_marker = 1
            self.root.ids.new_item_price.text = ''

        if new_item_name == '':
            self.root.ids.new_item_name_display.text = "New Item Name\n (Cannot be blank)"
        elif new_item_description == '':
            self.root.ids.new_item_description_display.text = "New Item Description\n(Cannot be blank)"
        elif error_marker == 1:
            self.root.ids.new_item_price_display.text = "Price per Day\n(Price must be a number)"

        else:
            NewItem = Item(new_item_name, new_item_description, new_item_price, 'in')
            self.items.add_new_item(NewItem)
            temp_button = Button(text=NewItem.name)
            temp_button.bind(on_release=self.press_entry)
            temp_button.background_color = (0, 0, 1, 1)
            self.root.ids.items_grid.add_widget(temp_button)
            self.root.ids.popup.dismiss()
            self.clear_fields()

    def clear_fields(self):
        # print("hi")
        self.root.ids.new_item_name.text = ''
        self.root.ids.new_item_description.text = ''
        self.root.ids.new_item_price.text = ''

    def press_cancel(self):
        """
        this closes the popup and calls the above function to clear the text fields so they are blank when
        it is opened again
        """
        self.root.ids.popup.dismiss()
        self.clear_fields()
        # self.status_text = ''

    def press_list(self):
        self.running_mode = 'list'
        current_item = self.items.return_all()
        current_item_position = self.items.find_item_logical_position(current_item)
        current_item_object = self.items.get_items(current_item_position)
        current_item_name = current_item_object.name
        current_item_description = current_item_object.description
        current_item_price = current_item_object.price
        current_item_status = current_item_object.status
        self.root.ids.status_text.text = "{} {} {} {}".format(current_item_name, current_item_description,
                                                              current_item_price, current_item_status)

    def press_hire(self):
        global TOTAL_HIRE_PRICE
        global HIRE_ITEM_LIST
        self.running_mode = 'hire'
        TOTAL_HIRE_PRICE = ''
        HIRE_ITEM_LIST = []
        hiring_items = self.items.return_all()
        HIRE_ITEM_LIST.append(hiring_items)
        self.root.ids.status_text.text = "{} {} {} {}".format("Hiring", HIRE_ITEM_LIST, "for", TOTAL_HIRE_PRICE)

    def press_return(self):
        global RETURN_ITEM_LIST
        self.running_mode = 'return'

        RETURN_ITEM_LIST = []
        returning_items = self.items.return_all()
        RETURN_ITEM_LIST.append(returning_items)
        self.root.ids.status_text.text = "{} {}".format("Returning: ", RETURN_ITEM_LIST)

    def press_confirm(self):
        self.confirm = 'confirm'
        on_press = self.confirm
        
        """Change colours of items, and status depending on mode"""

    def on_stop(self):
        final_list = self.items.return_all()
        write_string = " "
        for item in final_list:
            print(item)
            name = item.name
            description = item.description
            price = item.price
            availability = item.status
            final_item_string = "{},{},{},{}\n".format(name, description, price, availability)
            write_string = write_string + final_item_string
            print(write_string)

        save_file = open(filename, 'w')
        save_file.write(write_string)
        save_file.close()


MyApp().run()
