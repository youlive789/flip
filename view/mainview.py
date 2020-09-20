import sys
import ctypes
import keyboard
import win32gui
from pathlib import Path

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from view.systemtray import SystemTrayIcon

from transformers import EncoderDecoderModel, BertTokenizer, Trainer, TrainingArguments
import torch

from unicodedata import normalize

Builder.load_file("view/kv/main.kv")

class MainView(Screen):

    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)
        self.is_pressing = False
        Clock.schedule_once(lambda dt : self.prepare())

        # systemtray
        self.system_tray = SystemTrayIcon()

        # autohotkey
        self.ahk = ctypes.cdll.LoadLibrary("third-party/autohotkey-win/AutoHotKey.dll")
        self.ahk.ahktextdll(u"")

        # huggingface
        if getattr(sys, 'frozen', False):
            self.model = EncoderDecoderModel.from_pretrained(sys._MEIPASS + '\\third-party\\huggingface\\')
        else:
            self.model = EncoderDecoderModel.from_pretrained('./third-party/huggingface/')
            
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')

    def prepare(self):
        keyboard.hook(self.ctrl_pressed)
        Window.bind(on_request_close=self.minimize_window)

    def ctrl_pressed(self, e):
        app = App.get_running_app()
        if e.name == 'ctrl' and e.event_type == "down" and not self.is_pressing:
            self.is_pressing = True

            read_text = app.main_view_model.ocr.get_recognized_text()
            read_text = read_text.strip()

            input_ids = torch.tensor(self.tokenizer.encode(read_text, add_special_tokens=True)).unsqueeze(0).to(torch.device("cpu"))
            generated = self.model.generate(input_ids, decoder_start_token_id=self.model.config.decoder.pad_token_id)
            translated_text = self.tokenizer.decode(generated[0])
            translated_text = self.process_translated_text(translated_text)

            cmd = "ToolTip " + translated_text
            self.ahk.ahkExec(cmd)
        elif e.name == 'ctrl' and e.event_type == "up":
            self.ahk.ahkExec("ToolTip")
            self.is_pressing = False

    def process_translated_text(self, translated_text):
        translated_text = translated_text.replace("[PAD]", "")
        translated_text = translated_text.replace("[SEP]", "")
        translated_text = normalize('NFC', translated_text)
        return translated_text

    def minimize_window(self, *args):
        App.get_running_app().root_window.minimize()
        return True