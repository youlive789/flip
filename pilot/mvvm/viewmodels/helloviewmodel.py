from kivy.properties import NumericProperty
from kivy.event import EventDispatcher
from models.hello import Hello

class HelloViewModel(EventDispatcher):

    hello = Hello()