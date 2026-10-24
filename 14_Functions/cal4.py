import os
os.system('cls')

history = []

def addToHistory(data):
    """This function is used for add data into history."""
    history.append(data)

def showHistory():
    for data in history:
        print(data)

while True:
    print("""
Use these shortcuts for navigation:

q : use for close 
sh : use for show history
""")
    user = input("\nYou: ")

    if 'q' in user or 'exit' in user: break
    # if user in ['q', 'exit']: break

    elif 'sh' in user:
        showHistory()

    else:
        result = eval(user)
        print("Result: ", result)
        addToHistory(f"{user} : {result}")