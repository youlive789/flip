from kivy.properties import NumericProperty
from kivy.event import EventDispatcher
from models.hello import Hello

class HelloViewModel(EventDispatcher):

    hello = Hello()
    click_property = NumericProperty()
    
    def update_click_property(self, btn):
        print("버튼클릭", btn)
        self.click_property += 1