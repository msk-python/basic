import pyttsx3, os

e = pyttsx3.init()

e.setProperty('rate', 125)

voices = e.getProperty('voices')
e.setProperty('voice', voices[1].id)

def speak(text):
    e.say(text)
    e.runAndWait()

while True:
    import os
    os.system('cls')
    user = input("You: ")
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
        
    