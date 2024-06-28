import pyttsx3

e = pyttsx3.init()

rate = e.getProperty('rate')   # getting details of current speaking rate
# print(rate)                        #printing current voice rate
e.setProperty('rate', 125)

# Print all Voices in our computer 
voices = e.getProperty('voices')
# print(voices)       
e.setProperty('voice', voices[1].id)

def speak(text):
    e.say(text)
    e.runAndWait()

value = int(input("Enter a Value: "))

def check_even(value):
    return value % 2 == 0

if check_even(value):
    speak("This value is Even")
else:
    speak("This value is Odd")






