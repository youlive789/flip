from model.ocr import OCR
from kivy.event import EventDispatcher

class MainViewModel(EventDispatcher):
    ocr = OCR()