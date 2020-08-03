import cv2
import numpy as np

import matplotlib.pyplot as plt
import pygetwindow as gw
import win32gui

from PIL import ImageGrab, Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract'

# 마우스 정보 가져오기
flags, hcursor, (x,y) = win32gui.GetCursorInfo()
now_window = gw.getWindowsAt(x, y)[0]

# 이미지 캡쳐 범위설정 (마우스 커서 위치 창의 사이즈)
bb = (now_window.left, now_window.top, now_window.right, now_window.bottom)
img = ImageGrab.grab(bbox=bb)
rgb = np.array(img)

small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)

_, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

# cv2.imshow('rects', small)
# cv2.waitKey()
# quit()

# using RETR_EXTERNAL instead of RETR_CCOMP
contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
mask = np.zeros(bw.shape, dtype=np.uint8)

for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
    
    text = ""
    if w + h >= 50: 
        # 어떤 전처리 이미지에서 텍스트를 추출할 것인지 테스트 해봐야 한다.
        img = Image.fromarray(small[y:y+h, x:x+w])
        text = pytesseract.image_to_string(img, lang="kor+eng", config='--psm 7 --oem 1')
        print(text)

    if r > 0.3 and w > 8 and h > 8:
        cv2.rectangle(rgb, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)
        cv2.putText(rgb, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (36, 255, 12), 2)

# show image with contours rect
cv2.imshow('rects', rgb)
cv2.waitKey()