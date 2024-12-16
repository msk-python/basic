import pyttsx3   # pip install pyttsx3

while True:
    user = input('You: ')
    user = user.lower()
    
    if 'hi' in user :
        print('Bot: Hello') 
        pyttsx3.speak('Hello')
        
    elif 'how are you' in user:
        print('Bot: I am fine') 
        pyttsx3.speak('i am fine')
