from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview import RecycleView

Builder.load_file("views/kv/hello.kv")

class HelloView(Screen):

    def __init__(self, **kwargs):
        super(HelloView, self).__init__(**kwargs)

    

