import os, time, subprocess, pyautogui

class whatsapp:
    def open(wait=0.1, sleep=3) -> None:
        time.sleep(wait)
        subprocess.run(['start', 'whatsapp://'], shell=True)
        time.sleep(sleep)

    def close(wait:float=0.5) -> None:
        time.sleep(wait)
        subprocess.run(['taskkill', '/f', '/im', 'whatsapp.exe'], shell=True)

whatsapp.open()
time.sleep(2)
pyautogui.write("8954382678")
time.sleep(0.3)
pyautogui.press("down")
time.sleep(0.3)
pyautogui.press("enter")
time.sleep(0.3)
pyautogui.write("Hello, With Python")
time.sleep(0.2)
pyautogui.press("enter")
whatsapp.close()