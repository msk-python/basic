import os
import webbrowser

os.system('cls')

print("#------ Welcome to MSK Chat Bot --------#")

user = input("Enter You name : ")

print("Bot : Hello, " + user)
print("Bot : How may i help you dear, " + user)

user_chat = input("You : ")

if  "Hi" in user_chat:
    print("Bot : Hello")

elif "How are you" in user_chat:
    print("Bot : I am fine")

elif "help me" in user_chat:
    print("Bot : How can i help you. I work for you like open any software. ")
    print("Bot : Example:- Open YouTube, Open Google")

elif "open youtube" in user_chat:
    print("Bot : Opening Youtube")
    webbrowser.open("https://www.youtube.com/")

elif "open youtube" in user_chat:
    print("Bot : Opening Youtube")
    webbrowser.open("https://www.youtube.com/")

elif "open google" in user_chat:
    print("Bot : Opening Google")
    webbrowser.open("https://www.google.com/")

elif "open notepad" in user_chat:
    print("Bot : Opening Notepad")
    os.system('notepad')