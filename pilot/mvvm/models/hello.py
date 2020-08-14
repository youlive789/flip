import numpy as np
import win32gui

import cv2
from PIL import ImageGrab, Image

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
        x, y = self._get_mouse_pos()
        self.now_window = self._get_window_by_pos(x, y)

    def _get_window_by_pos(self, x, y):
        top_windows = []
        win32gui.EnumWindows(self._window_enumeration_handler, top_windows)
        for window in top_windows:
            x_low, y_low, x_high, y_high = window[1]
            x_in = x >= x_low and x <= x_high
            y_in = y >= y_low and y <= y_high
            if x_in and y_in and window[2] != '':
                return window[1]

    def _window_enumeration_handler(self, hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowRect(hwnd), win32gui.GetWindowText(hwnd)))

    def _set_now_screen(self):
        capture_box = (self.now_window[0], self.now_window[1], self.now_window[2], self.now_window[3])
        capture_img = ImageGrab.grab(bbox=capture_box)
        capture_img_numpy = np.array(capture_img)
        self.now_screen = capture_img_numpy

    def _set_cv2_processed_screen(self):
        self.now_screen = cv2.cvtColor(self.now_screen, cv2.COLOR_BGR2GRAY)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        grad = cv2.morphologyEx(self.now_screen, cv2.MORPH_GRADIENT, kernel)

        _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
        connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(connected, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
        self.cv2_processed_contours = contours

    def _get_mouse_pos(self):
        _, _, (x,y) = win32gui.GetCursorInfo()
        return x, y - 25

    def _get_mouse_pos_text(self, x_mouse, y_mouse):
        img = self._get_mouse_in_numpy_array_img(x_mouse, y_mouse)
        if img:
            text = pytesseract.image_to_string(img, lang="kor+eng", config='--psm 7 --oem 1')
        else:
            text = ""
        return text

    def _get_mouse_in_numpy_array_img(self, x_mouse, y_mouse):
        for idx in range(len(self.cv2_processed_contours)):
            x, y, w, h = cv2.boundingRect(self.cv2_processed_contours[idx])
            x_in = (x_mouse >= x) and (x_mouse <= x + w)
            y_in = (y_mouse >= y) and (y_mouse <= y + h)

            if x_in and y_in:
                img = Image.fromarray(self.now_screen[y:y+h, x:x+w])
                return img

        return None