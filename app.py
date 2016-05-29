from kivy.app import App
from kivy.lang import Builder
# from kivy.core.window import Window
from kivy.uix.button import Button
# from kivy.properties import StringProperty
from A2 import load_items
# from itemlist import get_item_names
from item import Item

filename = 'items.csv'
list_of_items = load_items(filename)
print(list_of_items)


# The custom App class
class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.items = Item()


# Creates the window and provides the basic information used in the start up of the program
    def build(self):
        # Window.size = (700, 700)
        self.title = "EquipmentHire"
        self.root = Builder.load_file('gui.kv')
        # self.create_entry_buttons()
        return self.root

    def create_entry_buttons(self):
        for items in self.items:
            temp_button = Button(text=items)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entriesBox.add_widget(temp_button)

    # def create_item_buttons(self):
    #     for items in self.items:


    # def press_entry(self, instance):
    #     items = instance.text
        # self.status_text = "{}'s number is {}".format(items, self.items[load_items()])
        # instance.state = 'down'

    # def press_clear(self):
    #     for instance in self.root.ids.entriesBox.children:
    #         instance.state = 'normal'
    #     self.status_text = ""

    def press_add(self):
        """
        this opens the popup for creating a new item entry
        """
        # self.status_text = "Enter details for new item"
        self.root.ids.popup.open()

    def press_save_new_item(self, new_item_name, new_item_description, new_item_price):
        self.items[new_item_name] = new_item_name, new_item_description, new_item_price
        self.root.ids.entriesBox.cols = len(self.items)
        # self.items[new_item_description] = new_item_description
        # self.root.ids.entriesBox.cols = len(self.items)
        # self.items[new_item_price] = new_item_price
        # self.root.ids.entriesBox.cols = len(self.items)
        temp_button = Button(text=new_item_name)
        temp_button.bind(on_release=self.press_entry)
        # self.root.ids.entriesBox.add_widget(temp_button)
        # self.root.ids.popup.dismiss()
        # self.clear_fields()

    def clear_fields(self):
        self.root.ids.newItem.text = ''
        self.root.ids.newItemDescription.text = ''
        self.root.ids.newItemPrice.text = ''

    def press_cancel(self):
        """
        this closes the popup and calls the above function to clear the text fields so they are blank when
        it is opened again
        """
        self.root.ids.popup.dismiss()
        self.clear_fields()
        # self.status_text = ''


MyApp().run()
