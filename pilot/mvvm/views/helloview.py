import keyboard
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.clock import Clock

Builder.load_file("views/kv/hello.kv")

class HelloView(Screen):

    def __init__(self, **kwargs):
        super(HelloView, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt : self.prepare())

    def prepare(self):
        # app = App.get_running_app()
        # app.hello_view_model.bind(
        #     click_property=lambda o,v: print(o,v)
        # )
        keyboard.hook(self.keyboard_test)

    def keyboard_test(self, e):
        app = App.get_running_app()
        for code in keyboard._pressed_events:
            if e.name == 'ctrl':
                print(app.hello_view_model.hello.get_recognized_text())