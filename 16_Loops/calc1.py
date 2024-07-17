h = []

def show_History():
    print("\n#--------------- History -------------#\n")
    for x in h:
        print("    " ,x)

    print("\n#--------------- End History -------------#\n")

while True:
    a = input("Enter value of A: ")
    if "q" in a:
        break
    elif "h" in a:
        show_History()
        continue

    o = input("Enter op: ")
    if "q" in o:
        break
    elif "h" in o:
        show_History()
        continue

    b = input("Enter value of B: ")
    if "q" in b:
        break
    elif "h" in b:
        show_History()
        continue

    if "+" in o:
        result = int(a) + int(b)
        print(f"{a} + {b} = {result}")
        h.append(f"{a} + {b} = {result}")
    elif "-" in o:
        result = int(a) - int(b)
        print(f"{a} - {b} = {result}")
        h.append(f"{a} - {b} = {result}")
    elif "*" in o:
        result = int(a) * int(b)
        print(f"{a} * {b} = {result}")
        h.append(f"{a} * {b} = {result}")
    elif "/" in o:
        result = int(a) / int(b)
        print(f"{a} / {b} = {result}")
        h.append(f"{a} / {b} = {result}")
    else:
        print("Invalid")

