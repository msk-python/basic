import os  # open
import subprocess # close

import time




# os.system('notepad')
# os.system('calc')
os.system('microsoft.windows.camera:')


# os.system(f'taskkill /f /im calc.exe')

time.sleep(30)

# subprocess.run(['taskkill', '/f', '/im', 'notepad.exe'], shell=True)
subprocess.run(['taskkill', '/f', '/im', 'microsoft.windows.camera:'], shell=True)
# subprocess.run(['taskkill', '/f', '/im', 'calc'], shell=True)
