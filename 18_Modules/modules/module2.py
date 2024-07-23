import pyttsx3, os 
import speech_recognition as sr # pip install SpeechRecognition


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
        print(f"You: {query_text}")
        return query_text.lower()
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


while True:    
    
    user = query()
    
    if 'exit' in user or 'bye' in user:
        pyttsx3.speak("Ok bye, Sir")
        break
    elif 'hi' in user:
        pyttsx3.speak("Hello how are you")
    elif 'open' in user:
        if 'excel' in user:
            pyttsx3.speak("Ok sir, opening excel")
            os.system('start excel')
            
        elif 'word' in user:
            pyttsx3.speak("Ok  sir, opening word")
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
            os.system('taskkill /f /im word.exe')
            
        elif 'powerpoint' in user:
            pyttsx3.speak("Ok sir, closing powerpoint")
            os.system('taskkill /f /im powerpnt.exe')
        
        elif 'whatsapp' in user:
            pyttsx3.speak("Ok sir, closing Whatsapp")
            os.system('taskkill /f /im whatsapp.exe')

    else:
        shutDown_Function(user)