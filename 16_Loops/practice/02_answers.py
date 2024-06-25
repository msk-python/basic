a = [3, 5, 6, 2, 7, 8, 6, 7, 8]



# 1. Write a program to find the largest number in a list of numbers.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Method 1: Using max() function
# ln = max(a)
# print(f"The largest number in the list is: {ln}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Method 2: Using a loop
# def largestNumber(numbers):
#     ln = numbers[0]
#     for number in numbers:
#         if number > ln:
#             ln = number
#     print(f"The largest number in the list is: {ln}")
# largestNumber(a)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 2. Write a program to find the smallest number in a list of numbers.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Method 1: Using min() function
# def smallestNumber(numbers):
#     sn = min(numbers)
#     print(f"The smallest number in the list is: {sn}")
# smallestNumber(a)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 3. Write a program to find the sum of all the numbers in a list.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# sum_of_numbers = sum(a)
# print(f"Sum of all numbers: {sum_of_numbers}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# 4. Write a program to find the average of a list of numbers.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# average = sum(a) / len(a)
# print(f"Average of numbers: {average}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# 5. Write a program to find the second largest number in a list of numbers.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# sorted_list = sorted(a, reverse=True)
# print(sorted_list)
# second_largest = sorted_list[1]
# print(f"Second largest number: {second_largest}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 6. Write a program to count the number of even numbers in a list.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def countEven(value):
#     total = 0
#     for number in value :
#         if number % 2 == 0:
#             total += 1
#     print("Count of even numbers: ", total)
#     return total

# countEven(a)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 7. Write a program to count the number of odd numbers in a list.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def countEven(value):
#     total = 0
#     for number in value :
#         if number % 2 != 0:
#             total += 1
#     print("Count of odd numbers: ", total)
#     return total

# countEven(a)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

