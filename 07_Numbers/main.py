import random

while True:
    x = random.randrange(111111, 999999)
    print(x)
    y = int(input("Enter Your OTP: "))

    if x == y:
        print("OTP Valid: ✅")
        break
    else:
        print("\nPlease try again: ❌\n")
        continue

print("Welcome to Website")