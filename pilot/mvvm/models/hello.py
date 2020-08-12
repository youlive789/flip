import cv2
import numpy as np
from PIL import ImageGrab, Image
import pygetwindow as gw
import win32gui

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'

class Hello:
    
    now_window = None
    now_screen = None
    cv2_processed_contours = None

    def get_recognized_text(self):
        self._set_now_cv2_screen()
        x, y = self._get_mouse_pos()
        text = self._get_mouse_pos_text(x, y)
        return text

    def _set_now_cv2_screen(self):
        self._set_now_window()
        self._set_now_screen()
        self._set_cv2_processed_screen()
        
    def _set_now_window(self):
        _, _, (x,y) = win32gui.GetCursorInfo()
        self.now_window = gw.getWindowsAt(x,y)[0]

    def _set_now_screen(self):
        capture_box = (self.now_window.left, self.now_window.top, self.now_window.right, self.now_window.bottom)
        capture_img = ImageGrab.grab(bbox=capture_box)
        capture_img_numpy = np.array(capture_img)
        self.now_screen = capture_img_numpy

    def _set_cv2_processed_screen(self):
        self.now_screen = cv2.cvtColor(self.now_screen, cv2.COLOR_BGR2GRAY)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        grad = cv2.morphologyEx(self.now_screen, cv2.MORPH_GRADIENT, kernel)

        _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
        connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(connected, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
        self.cv2_processed_contours = contours

    def _get_mouse_pos(self):
        _, _, (x,y) = win32gui.GetCursorInfo()
        return x, y

    def _get_mouse_pos_text(self, x_mouse, y_mouse):
        for idx in range(len(self.cv2_processed_contours)):
            x, y, w, h = cv2.boundingRect(self.cv2_processed_contours[idx])
            x_in = (x_mouse >= x) and (x_mouse <= x + w)
            y_in = (y_mouse >= y) and (y_mouse <= y + h)

            if x_in and y_in:
                img = Image.fromarray(self.now_screen[y:y+h, x:x+w])
                text = pytesseract.image_to_string(img, lang="kor+eng", config='--psm 7 --oem 1')
                return text
            else:
                continue

        return ''