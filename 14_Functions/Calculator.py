import os 
os.system('cls')

def show():
    os.system('cls')
    file = open("17_Functions/history.txt", 'r')
    print("\n#------------------ History ------------------# \n")
    for x in file:
        print(x)
    print("\n#------------------ End History ------------------# \n")
    file.close()

def clear():
    file = open("17_Functions/history.txt", "w")
    file.write("")
    file.close()
    os.system('cls')
    print("All History Clear")

def update_history(value):
    file = open("17_Functions/history.txt", "a")
    file.write(value)
    file.close()

#------------------------------------ Start While loop ------------------------------------#
while True:
    a = input("\nEnter a value: ")
    if "q" in a:
        os.system('cls')
        print("#------------------ Thanks for Using Me ------------------#\n")
        break
    elif "h" in a:
        show()
        continue
    elif "c" in a:
        clear()
        continue

    #------------------------------ Result Calculation -------------------#
    result = eval(a)
    os.system('cls')
    print(f'{a} : {result}')
    update_history(f'{a} : {result}\n')
    #------------------------------ End Result Calculation -------------------#
#------------------------------------ End While loop ------------------------------------#
