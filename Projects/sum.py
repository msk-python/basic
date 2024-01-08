while True:
    print("\nPress ( q ) for exit from while loop\n")
    x = input("Enter x Value: ")
    if "q" in x:
        break
    y = input("Enter y Value: ")
    x = int(x)  
    y = int(y)
    sum = x+y
    div = x/y
    min = x*y
    sub = x-y
    print("sum value of x, y : ", sum)
    print("div value of x, y : ", div)
    print("min value of x, y : ", min)
    print("sub value of x, y : ", sub)
print("\n#----Thank You for use me------#\n")