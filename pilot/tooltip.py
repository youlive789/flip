import win32con, win32gui
from win32api import GetModuleHandle
from commctrl import (TOOLTIPS_CLASS, TTS_ALWAYSTIP, TTS_NOPREFIX, TTM_ADDTOOL, TTM_SETMAXTIPWIDTH)

class TooltipWindow:
    def __init__(self):
        win32gui.InitCommonControls() # Loads COMCTL32.DLL (Shell Common Controls Library)
        self.hwnd = win32gui.CreateWindowEx(
            win32con.WS_EX_CLIENTEDGE | win32con.WS_EX_TOPMOST,
            TOOLTIPS_CLASS,
            "MyTooltipWindow",
            win32con.WS_POPUP | TTS_ALWAYSTIP | TTS_NOPREFIX | win32con.WS_BORDER,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            None,
            None,
            GetModuleHandle(None),
            None
        )

        win32gui.SetWindowPos(self.hwnd, win32con.WS_EX_TOPMOST, 0, 0, 0, 0, 
                        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE)

        win32gui.SendMessage(self.hwnd, TTM_ADDTOOL, None, 0)

if __name__ == "__main__":
    # tooltip = TooltipWindow()
    import ctypes
    dll = ctypes.cdll.LoadLibrary("../third-party/autohotkey-win/AutoHotkey.dll")
    dll.ahktextdll(u"")
    dll.ahkExec('MouseGetPos, xPos, yPos, winId' \
'\n    PixelGetColor, color, %xPos%, %yPos%' \
'\n    WinGetTitle winTitle, ahk_id %winId%' \
'\n    ToolTip "%winTitle%"`n%xPos% %yPos% %color%')
    dll.ahkExec('sleep 5000')
    