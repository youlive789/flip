import win32gui
def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowRect(hwnd), win32gui.GetWindowText(hwnd)))

if __name__ == "__main__":
    results = []
    top_windows = []

    _, _, (x, y) = win32gui.GetCursorInfo()
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        x_low, y_low, x_high, y_high = i[1]
        x_in = x >= x_low and x <= x_high
        y_in = y >= y_low and y <= y_high
        if x_in and y_in and i[2] != '':
            print(i)
            break