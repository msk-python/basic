import os, webbrowser
from speaker import speak
from voiceToText import query

speak("Welcome to MSK", True)

while True:
    hotword = query(word="Listening...", Said="You")
    os.system('cls')
    if "jarvis" in hotword or "Jarvis" in hotword:
        speak("Yes Sir", True)

        while True:
            user = query(word="==> Jarvis Listening...", Said="You Said")
            if "ok bye" in user or 'close' in user:
                speak("Ok bye", True)
                break
            if "open youtube" in user:
                speak("Opening Youtube...", True)
                webbrowser.open_new_tab("youtube.com")
            elif "open file manager" in user:
                os.system('explorer')
            elif "open notepad" in user or "notepade" in user:
                speak("Opening Notepad...", True)
                os.system("notepad")
