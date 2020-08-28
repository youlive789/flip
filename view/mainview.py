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

import torch
from transformers import EncoderDecoderModel, BertTokenizer

Builder.load_file("view/kv/main.kv")

class MainView(Screen):

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.system_tray = SystemTrayIcon()
        self.is_pressing = False
        Clock.schedule_once(lambda dt : self.prepare())
        self.ahk = ctypes.cdll.LoadLibrary("third-party/autohotkey-win/AutoHotKey.dll")
        self.ahk.ahktextdll(u"")
        self.model = EncoderDecoderModel.from_pretrained('third-party/huggingface/')
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')

    def prepare(self):
        keyboard.hook(self.ctrl_pressed)
        Window.bind(on_request_close=self.minimize_window)

    def ctrl_pressed(self, e):
        app = App.get_running_app()
        if e.name == 'ctrl' and e.event_type == "down" and not self.is_pressing:
            self.is_pressing = True

            read_text = app.main_view_model.ocr.get_recognized_text()
            print("인식 : ", read_text)

            input_ids = torch.tensor(self.tokenizer.encode(read_text, add_special_tokens=True)).unsqueeze(0).to(torch.device("cpu"))
            generated = self.model.generate(input_ids, decoder_start_token_id=self.model.config.decoder.pad_token_id)
            translated = self.tokenizer.decode(generated[0])

            translated = translated.replace("[PAD]", "")
            translated = translated.replace("[SEP]", "")
            print("번역 : ", translated)

            self.ahk.ahkExec("ToolTip " + translated)
        elif e.name == 'ctrl' and e.event_type == "up":
            self.ahk.ahkExec("ToolTip")
            self.is_pressing = False

    def minimize_window(self, *args):
        App.get_running_app().root_window.minimize()
        return True