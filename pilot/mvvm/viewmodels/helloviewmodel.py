from kivy.properties import BoundedNumericProperty
from kivy.event import EventDispatcher

class HelloViewModel(EventDispatcher):
    click_property = BoundedNumericProperty(1, min=0, max=5)
    
    def update_click_property(self, btn):
        print("들어옴", btn)
        self.click_property += 1