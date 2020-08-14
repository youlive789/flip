import keyboard

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_file("view/kv/main.kv")

class MainView(Screen):

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.is_pressing = False
        Clock.schedule_once(lambda dt : self.prepare())

    def prepare(self):
        keyboard.hook(self.ctrl_pressed)

    def ctrl_pressed(self, e):
        app = App.get_running_app()
        if e.name == 'ctrl' and e.event_type == "down" and not self.is_pressing:
            self.is_pressing = True
            print(app.main_view_model.ocr.get_recognized_text())
        elif e.name == 'ctrl' and e.event_type == "up":
            self.is_pressing = False