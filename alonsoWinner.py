import time
import os
os.environ['DISPLAY'] = ':0'
os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'
import pyautogui,time
from pywinauto.application import Application

teclado = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

def openChrome():
    return Application().start('chrome.exe')

def maximizeApp():
    pyautogui.hotkey(teclado[186], teclado[182])
    pyautogui.hotkey(teclado[186], teclado[182])

def goTo(x:int, y:int, seconds:int = 0.5):
    pyautogui.moveTo(x, y, seconds)
    time.sleep(0.5)
    pyautogui.click()




chrome = openChrome()
while True:
    time.sleep(0.5)
    pyautogui.hotkey(teclado[90],teclado[175], teclado[55])
    time.sleep(0.5)
    maximizeApp()
    pyautogui.typewrite(str('https://t.co/XdpxNzMEFD'))
    pyautogui.press(teclado[98])
    time.sleep(2.5)
    goTo(970, 800)
    time.sleep(0.8)
    pyautogui.press(teclado[96],35)
    goTo(620, 460)
    print('Otro puntito para el Nano!')
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.5)

# https://t.co/XdpxNzMEFD
