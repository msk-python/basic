import pyttsx3, os

e = pyttsx3.init()

rate = e.getProperty('rate')         # getting details of current speaking rate
# print(rate)                        # printing current voice rate
e.setProperty('rate', 125)

# Print all Voices in our computer 
voices = e.getProperty('voices')
# print(voices)       
e.setProperty('voice', voices[1].id)

def speak(text):
    e.say(text)
    e.runAndWait()

speak("Hello how are you")
    