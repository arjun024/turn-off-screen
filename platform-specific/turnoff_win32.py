import win32gui
import win32con

SC_MONITORPOWER = 0xF170
win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)