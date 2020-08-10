from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview import RecycleView

# kv = ""
# Builder.load(kv)

class HelloStream(RecycleView):
    pass

class HelloView(Screen):

    def __init__(self, **kwargs):
        super(HelloView, self).__init__(**kwargs)

    

