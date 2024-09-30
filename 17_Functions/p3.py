history = []

while True:
    a = int(input("Enter value of A : "))
    o = input("Enter Operator: ")
    b = int(input("Enter value of B : "))

    if o == "+":
        result = a + b
        print("Result :", result)
        history.append(f"{a} + {b} : {result}")

    elif o == "-":
        result = a - b
        print("Result :", result)
        history.append(f"{a} - {b} : {result}")
        
    elif o == "*":
        result = a * b
        print("Result :", result)
        history.append(f"{a} * {b} : {result}")
