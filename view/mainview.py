import ctypes
import keyboard
import win32gui

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

Builder.load_file("view/kv/main.kv")

class MainView(Screen):

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.is_pressing = False
        Clock.schedule_once(lambda dt : self.prepare())
        self.ahk = ctypes.cdll.LoadLibrary("third-party/autohotkey-win/AutoHotKey.dll")
        self.ahk.ahktextdll(u"")

    def prepare(self):
        keyboard.hook(self.ctrl_pressed)

    def ctrl_pressed(self, e):
        app = App.get_running_app()
        if e.name == 'ctrl' and e.event_type == "down" and not self.is_pressing:
            self.is_pressing = True
            read_text = app.main_view_model.ocr.get_recognized_text()
            print(read_text)
            self.ahk.ahkExec("ToolTip " + read_text)
        elif e.name == 'ctrl' and e.event_type == "up":
            self.ahk.ahkExec("ToolTip")
            self.is_pressing = False