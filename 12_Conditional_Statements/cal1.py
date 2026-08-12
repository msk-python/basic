
val_1 = int( input( "Enter value of A : "))
o =          input( "Enter Operator: ")
val_2 = int( input( "Enter value of B : "))

if "+" in o:
    print("Result :", val_1 + val_2)
elif "-" in o:
    print("Result :", val_1 - val_2)
elif "*" in o:
    print("Result :", val_1 * val_2)
elif "/" in o:
    print("Result :", val_1 / val_2)
elif "//" in o:
    print("Result :", val_1 // val_2)
elif "**" in o:
    print("Result :", val_1 ** val_2)
