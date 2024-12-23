# Python program to calculate simple interest

def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Take user input for principal amount, rate, and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest
interest = simple_interest(principal, rate, time)

# Display the simple interest
print("Simple interest:", interest)