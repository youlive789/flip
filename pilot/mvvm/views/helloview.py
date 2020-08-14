import keyboard
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.clock import Clock

Builder.load_file("views/kv/hello.kv")

class HelloView(Screen):

    def __init__(self, **kwargs):
        super(HelloView, self).__init__(**kwargs)
        self.is_pressing = False
        Clock.schedule_once(lambda dt : self.prepare())

    def prepare(self):
        # app = App.get_running_app()
        # app.hello_view_model.bind(
        #     click_property=lambda o,v: print(o,v)
        # )
        keyboard.hook(self.keyboard_test)

    def keyboard_test(self, e):
        app = App.get_running_app()
        if e.name == 'ctrl' and e.event_type == "down" and not self.is_pressing:
            self.is_pressing = True
            print(app.hello_view_model.hello.get_recognized_text())
        elif e.name == 'ctrl' and e.event_type == "up":
            self.is_pressing = False