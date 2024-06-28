import pyttsx3


def speak(text):
    e = pyttsx3.init()
    e.say(text)
    e.runAndWait()

speak("this is good")