import pyautogui
from time import sleep

# Ctrl + left click on this 👇 link for more update 
# https://pyautogui.readthedocs.io/_/downloads/en/latest/pdf/?utm_source=pyautogui&utm_content=flyout

['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
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


#--------------------------- Message Box Functions ---------------------------------#
# pyautogui.alert(text='Hello', title='How Are You', button='OK')
# a = pyautogui.confirm(text='Do you want to confirm this', title='Check', buttons=['Yes', 'No'])
# a = pyautogui.prompt(text='Please enter name: ', title='Log In' , default='MSK !nstitute')
# a = pyautogui.password(text='Enter Your Password', title='LogIn', default='', mask='*')



#--------------------------- Keyboard Functions ---------------------------------#
# pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1', 'esc'], interval=0.5)
# pyautogui.hotkey('win', 'i') # Open Settings
# sleep(3)                        # wait
# pyautogui.hotkey('alt', 'f4') # Close Settings

# hk = pyautogui.hotkey
# pr = pyautogui.press
# wr = pyautogui.write
# pyautogui.keyDown('shift') # hold down the shift key
# pyautogui.press('left') # press the left arrow key
# pyautogui.press('left') # press the left arrow key
# pyautogui.press('left') # press the left arrow key
# pyautogui.keyUp('shift') 


# a = pyautogui.size()            # return : screen resolution size
# a = pyautogui.position()      # return : current X and Y coordinates of the mouse cursor


# Screenshot Functions
# a = pyautogui.screenshot() # returns a Pillow/PIL Image object
pyautogui.screenshot('MSK.png') # returns a Pillow/PIL Image object, and saves it to a file

# print(a)