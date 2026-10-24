while True:
    a = int(input("Enter value of A : "))
    b = int(input("Enter value of B : "))
    o = input("Enter Operator: ")

    if o == "+":
        print("Result :", a + b)
    elif o == "-":
        print("Result :", a - b)
    elif o == "*":
        print("Result :", a * b)
    elif o == "/":
        print("Result :", a / b)
    elif o == "//":
        print("Result :", a // b)
    elif o == "**":
        print("Result :", a ** b)