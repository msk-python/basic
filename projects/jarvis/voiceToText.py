import speech_recognition as sr # pip install SpeechRecognition, pip install pyaudio

def query(word:str, Said:str=""):
    r = sr.Recognizer()
    r.energy_threshold = 500  
    r.pause_threshold = 1
    with sr.Microphone() as mic:
        print(word)
        audio = r.listen(mic)
    try:
        query_text = r.recognize_google(audio, language="en-IN")
        if Said is not None:
            print(f"{Said}: {query_text}")
        return query_text.lower()
    except sr.UnknownValueError:
        print('==> Sorry, I could not understand what you said.')
        return "None"
    except Exception as e:
        print(f"==> Error: {e}")
        return "None"


if __name__ == "__main__":
    myVoice =  query()
    print(myVoice)

