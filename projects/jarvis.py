import pyttsx3, os, webbrowser
import speech_recognition as sr   

# https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe

# pip install speechRecognition 
# pip install PyAudio
# pip install datefinder

e = pyttsx3.init()
e.setProperty('rate', 125)
voices = e.getProperty('voices')
e.setProperty('voice', voices[0].id)

def speak(text):
    pyttsx3.speak(text)
    return


def query():
    r = sr.Recognizer()
    r.energy_threshold = 500  
    r.pause_threshold = 1
    print('==> Listening...')
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        query_text = r.recognize_google(audio, language="en-IN")
        print(f"English: {query_text}")
        return query_text.lower()
    except sr.UnknownValueError:
        print('==> Sorry, I could not understand what you said.')
        return "None"
    except Exception as e:
        print(f"==> Error: {e}")
        return "None"

if __name__ == "__main__":
    while True:
        import os
        os.system('cls')
        user = query()
        bot = ""
        if "hi" in user:
            bot = "Hello"
            print("Bot: " , bot)
            speak(bot)
        elif "notepad" in user:
            bot = "Ok, Opening Notepad"
            print("Bot: " , bot)
            speak(bot)
            os.system("notepad")
        elif "calc" in user:
            bot = "Ok, Opening Calculator"
            print("Bot: " , bot)
            speak(bot)
            os.system("calc")
        elif 'excel' in user:
            bot = "Ok Sir, Opening Excel"
            print("Bot: ", bot)
            speak(bot)
            os.system('start excel')
        elif 'youtube' in user:
            webbrowser.open('www.youtube.com')
        elif 'bye' in user or 'ok bye' in user or 'bay' in user:
            bot = "Ok, Good bye sir"
            print("Bot: ", bot)
            speak(bot)
            break
