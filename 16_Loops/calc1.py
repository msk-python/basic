
while True:

    a = int(input("Enter value of A: "))
    o = input("Enter op: ")
    if "q" in o:
        break
    b = int(input("Enter value of B: "))

    if "+" in o:
        print(a + b)
    elif "-" in o:
        print(a - b)
    elif "*" in o:
        print(a * b)
    elif "/" in o:
        print(a / b)
    else:
        print("Invalid")
