import os 
os.system('cls')

h = []

class history():

    def show():
        os.system('cls')
        x = len(h)
        if x == 0:
            print("\n#------------------ History -------------------# \n")
            print("History is Empty")
        else:
            print("\n#------------------ History -------------------# \n")

            for x in h:
                print("    " , x)
                
            print("\n#------------------ End History -------------------# \n")

    def clear():
        h.clear()
        os.system('cls')
        print("All History Clear")
    
while True:
    a = input("\n Enter a value of A :")
    if "q" in a:
        os.system('cls')
        print("#----------------------- Thanks for Using ----------------------#\n")
        break
    elif "r" in a:
        continue
    elif "h" in a:
        history.show()
        continue
    elif "c" in a:
        history.clear()
        continue

    o = input("\n Enter a value of o : ")
    if "q" in o:
        os.system('cls')
        print("#----------------------- Thanks for Using ----------------------#\n")
        break
    elif "r" in o :
        continue      
    elif "h" in o:
        history.show()
        continue
    elif "c" in o:
        history.clear()
        continue

    b = input("\n Enter a value of b :")
    if "q" in b:
        os.system('cls')
        print("#----------------------- Thanks for Using ----------------------#\n")
        break 
    elif "r" in b:
        continue
    elif "h" in b:
        history.show()
        continue
    elif "c" in b:
        history.clear()
        continue


    if '+' in o :
        os.system("cls")
        result = int(a)+int(b)
        h.append(f"{a}+{b}: {result} ")
        print("\n Result : " , result )

    elif "-" in o:
        os.system("cls")
        result = int(a)-int(b)
        h.append(f"{a}-{b}: {result} ")
        print("\nResult :" , result)

    elif "*" in o:
        os.system("cls")
        result = int(a)*int(b)
        h.append(f"{a}*{b}: {result} ")
        print("\n Result :", result )

    elif "/" in o:
        os.system("cls")
        result = int(a)/int(b)
        h.append(f"{a}/{b}: {result} ")
        print("\n Result : " , result )
