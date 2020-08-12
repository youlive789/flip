from kivy.properties import BoundedNumericProperty
from kivy.event import EventDispatcher
from models.hello import Hello

class HelloViewModel(EventDispatcher):

    hello = Hello()
    click_property = BoundedNumericProperty(1, min=0, max=5)
    
    def update_click_property(self, btn):
        print("버튼클릭", btn)
        self.click_property += 1