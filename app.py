from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


# The custom App class
class MyApp(App):
    def __init__(self, **kwargs):
        super(EquipmentHire, self).__init__(**kwargs)
        self.details = Details()


# Creates the window and provides the basic informaiton used in the start up of the program
    def build(self):
        Window.size = (700, 700)
        self.title = "EquipmentHire"
        self.root = Builder.load_file('gui.kv')
        # self.

    def find_items(self):

    def add_new_item(self):


#         Create and start the app
EquipmentHire().run()