#!/usr/bin/env python
import sys
if sys.platform.startswith('linux'):
	import os
	os.system("xset dpms force off")
elif sys.platform.startswith('win'):
	import win32gui
	import win32con
	SC_MONITORPOWER = 0xF170
	win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2)
elif sys.platform.startswith('darwin'):
       import subprocess
        subprocess.call('echo \'tell application "Finder" to sleep\' | osascript', shell=True)
