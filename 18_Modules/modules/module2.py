import pyttsx3, os 
import speech_recognition as sr # pip install SpeechRecognition
import time, subprocess, pyautogui, webbrowser

e = pyttsx3.init()

# print(e.getProperty('rate'))    # printing current voice rate (speed)
print(e.getProperty('voices'))  # Print all Voices in our computer 

e.setProperty('rate', 250)  # Set voice rate (speed)

voices = e.getProperty('voices')
e.setProperty('voice', voices[2].id)

os.system('cls')


def query():
    r = sr.Recognizer()
    r.energy_threshold = 500  
    r.pause_threshold = 1
    with sr.Microphone() as source:
        print('==> Listening...')
        audio = r.listen(source)
    try:
        query_text = r.recognize_google(audio, language="en-IN")
        query = query_text.lower()
        print(f"You: {query}")
        return query
    except sr.UnknownValueError:
        print('==> Sorry, I could not understand what you said.')
        return "None"
    except Exception as e:
        print(f"==> Error: {e}")
        return "None"


def shutDown_Function(string:str):
    try:
        minute = float(''.join(filter(str.isdigit, string)))
        sec = minute * 60
    except Exception:
        sec = 0
    
    c_list = {
        "log out" : "shutdown -l",
        "sleep" : "Rundll32.exe powrprof.dll,SetSuspendState Sleep",
        
        "shutdown" : {
            "now" : "shutdown /s /t 0",
            'minute' : f"shutdown /s /t {int(sec)}",
            "stop" : "shutdown.exe /a",
        },
        
        "restart" : {
            'now' : "shutdown /r /t 0",
            'minute' : f"shutdown /r /t {int(sec)}",
            "stop" : "shutdown.exe /a",
        },
        
        "Hibernate immediately" : "shutdown /h /t 0",   
    }
    
    if 'shutdown' in string:
        if 'now' in string: 
            os.system(f"start {c_list['shutdown']['now']}") 
            print('shutdown now')
        elif 'minute' in string:
            os.system(f"start {c_list['shutdown']['minute']}")
            print(f'shutdown after {minute}')
        elif 'stop' in string: 
            print('shutdown stop')
            os.system(f"start {c_list['shutdown']['stop']}")
    elif 'restart' in string:
        if 'now' in string: 
            os.system(f"start {c_list['restart']['now']}")
            print('restart now')
        elif 'minute' in string:
            os.system(f"start {c_list['restart']['minute']}")
            print(f'restart after {minute}')
        elif 'stop' in string:
            os.system(f"start {c_list['restart']['stop']}")
            print(f'restart stop')
    else:
        if 'sleep' in string: os.system(f"start {c_list['sleep']}")

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

    def send_msg(command) -> None: 
        '''
        command : send massege to sachin rajput on whatsapp Hello, With python
        '''
        user = str(command)
        try:
            ind_to = user.index('tu')
        except:
            ind_to = user.index('to')
        ind_on = user.find('on')
        
        recevier_name = user[ind_to+3:ind_on-1]
        massege = user[ind_on+12:]
            
        if recevier_name in contact_list:
            contact = contact_list[recevier_name]
            whatsapp.open()
            time.sleep(2)
            pyautogui.write(contact)
            time.sleep(0.5)
            pyautogui.press("down")
            time.sleep(0.5)
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.write(massege)
            time.sleep(0.3)
            pyautogui.press("enter")
            whatsapp.close()
        else: print('This No not in your contact number:')
            
contact_list = {
    'sagar yadav': '8273269342',
    'sachin rajput': '9870941367',
}



def commands(user):

    if 'open' in user:
        if 'excel' in user:
            pyttsx3.speak("Ok sir, opening excel")
            os.system('start excel')
        elif 'word' in user:
            pyttsx3.speak("Ok sir, opening word")
            os.system('start winword')
        elif 'powerpoint' in user:
            pyttsx3.speak("Ok sir, opening powerpoint")
            os.system('start powerpnt')
        elif 'whatsapp' in user:
            pyttsx3.speak("Ok sir, opening whatsapp")
            os.system('start whatsapp://')     
    elif 'close' in user:
        if 'excel' in user:
            pyttsx3.speak("Ok sir, closing excel")
            os.system('taskkill /f /im excel.exe')
        elif 'word' in user:
            pyttsx3.speak("Ok sir, closing word")
            os.system('taskkill /f /im winword.exe')
        elif 'powerpoint' in user:
            pyttsx3.speak("Ok sir, closing powerpoint")
            os.system('taskkill /f /im powerpnt.exe')
        elif 'whatsapp' in user:
            pyttsx3.speak("Ok sir, closing Whatsapp")
            os.system('taskkill /f /im whatsapp.exe')
    elif 'send' in user and 'whatsapp' in user:
        whatsapp.send_msg(user)
    else:
        shutDown_Function(user)

while True:
    commands(query())
    
