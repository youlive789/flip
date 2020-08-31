import ctypes
import keyboard
import win32gui

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from view.systemtray import SystemTrayIcon

import chardet
import unidecode

Builder.load_file("view/kv/main.kv")

class MainView(Screen):

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.system_tray = SystemTrayIcon()
        self.is_pressing = False
        Clock.schedule_once(lambda dt : self.prepare())
        self.ahk = ctypes.cdll.LoadLibrary("third-party/autohotkey-win/AutoHotKey.dll")
        self.ahk.ahktextdll(u"")

    def prepare(self):
        keyboard.hook(self.ctrl_pressed)
        Window.bind(on_request_close=self.minimize_window)

    def ctrl_pressed(self, e):
        app = App.get_running_app()
        if e.name == 'ctrl' and e.event_type == "down" and not self.is_pressing:
            self.is_pressing = True

            read_text = app.main_view_model.ocr.get_recognized_text()
            read_text = read_text.strip()
            print(read_text)

            cmd = "ToolTip " + read_text
            print(cmd)
            self.ahk.ahkExec(cmd)
        elif e.name == 'ctrl' and e.event_type == "up":
            self.ahk.ahkExec("ToolTip")
            self.is_pressing = False

    def minimize_window(self, *args):
        App.get_running_app().root_window.minimize()
        return True