import time, subprocess, pyautogui, webbrowser

class whatsapp:
    def open(wait=0.1, sleep=3) -> None:
        time.sleep(wait)
        try:
            subprocess.run(['start', 'whatsapp://'], shell=True)
        except:
            webbrowser.open_new("https://web.whatsapp.com/")
        time.sleep(sleep)

    def close(wait:float=0.5) -> None:
        time.sleep(wait)
        subprocess.run(['taskkill', '/f', '/im', 'whatsapp.exe'], shell=True)

    def send_msg(contact_no, message, loop:int) -> None: 
        whatsapp.open()
        time.sleep(2)
        pyautogui.write(contact_no)
        time.sleep(0.5)
        pyautogui.press("down")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)
        pyautogui.write(message)
        time.sleep(0.3)
        pyautogui.press("enter")
        if loop:
            for i in range(loop):
                pyautogui.write(message)
                time.sleep(0.3)
                pyautogui.press("enter")
            whatsapp.close()

if __name__ == "__main__":
    whatsapp.send_msg("7505563288", "Hello", loop=1000)
