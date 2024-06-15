import os 

while True:
    print("Press (q) for exit: ")
    x = input("Enter value: ")

    if "q" in x:
        os.system('cls')
        print("#-------------------- Thanks for using -----------------#")
        break

    print("Loop Continue")