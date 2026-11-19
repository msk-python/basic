import pyttsx3 # pip install pyttsx3

e = pyttsx3.init()
e.setProperty('rate', 125)
voices = e.getProperty('voices')
e.setProperty('voice', voices[0].id)

def speak(text:str, output=False):
    if output is True:
        print("Bot:", text)
    pyttsx3.speak(text)
    return

if __name__ == "__main__":
    speak('This is a test after modifiy.')
