from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.properties import StringProperty
from A2 import load_items


# The custom App class
class MyApp(App):

    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        # self.items = {load_items}


# Creates the window and provides the basic information used in the start up of the program
    def build(self):
        # Window.size = (700, 700)
        self.title = "EquipmentHire"
        self.root = Builder.load_file('gui.kv')
        self.create_entry_buttons()
        return self.root

    # def create_entry_buttons(self):
    #     for items in self.items:
    #         temp_button = Button(text=items)
    #         temp_button.bind(on_release=self.press_entry)
    #         self.root.ids.entriesBox.add_widget(temp_button)
    #
    # def press_entry(self, instance):
    #     items = instance.text
    #     self.status_text = "{}'s number is {}".format(items, self.items[load_items()])
    #     instance.state = 'down'
    #
    # def press_clear(self):
    #     for instance in self.root.ids.entriesBox.children:
    #         instance.state = 'normal'
    #     # self.status_text = ""
    #
    # def press_add(self):
    #     self.status_text = "Enter details for new item"
    #     self.root.ids.popup.open()
    #
    # def press_save(self, newItem, newItemDescription, newItemPrice):
    #     self.items[newItem] = newItem
    #     self.root.ids.entriesBox.cols = len(self.items)
    #     temp_button = Button(text=newItem)
    #     temp_button.bind(on_release=self.press_entry)
    #     self.root.ids.entriesBox.add_widget(temp_button)
    #     self.root.ids.popup.dismiss()
    #     self.clear_fields()
    #
    # def clear_fields(self):
    #     self.root.ids.newItem.text = ''
    #     self.root.ids.newItemDescription.text = ''
    #     self.root.ids.newItemPrice.text = ''
    #
    # def press_cancel(self):
    #     self.root.ids.popup.dismiss()
    #     self.clear_fields()
        # self.status_text = ''


    # def load_items(self):
    #     return self


    # def add_new_item(self):


    # Create and start the app

MyApp().run()
