import pyttsx3

e = pyttsx3.init()
e.setProperty('rate', 125)
voices = e.getProperty('voices')
e.setProperty('voice', voices[2].id)

def speak(text):
    pyttsx3.speak(text)
    return