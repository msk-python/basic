# 1. How do you find the length of a string in Python?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "mskinstitute"
# length = len(s)
# print(f"The length of the string is: {length}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 2. Write a program to reverse a string in Python.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "mskinstitute"
# reversed_s = s[::-1]
# print(f"Reversed string : {reversed_s}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 3. How can you check if a string is a palindrome in Python?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "madam" # racecar, level, rotor, noon, mom, wow, pop, refer, stats
# is_palindrome = s == s[::-1]
# print(f"Is the string a palindrome? {is_palindrome}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 4. How do you count the number of vowels in a given string?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "mskinstitute"
# vowels = "aeiou"
# def countVowels(text):
#     totalVoweles = 0
#     for char in text:
#         if char.lower() in vowels:
#             totalVoweles += 1
#     print(totalVoweles)

# countVowels(s)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 5. Write a function to replace all occurrences of a substring in a string with another substring.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "hello world"
# new_s = s.replace("world", "Python")
# print(f"The new string is: {new_s}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#---------------- Print only-one table ----------------------#
# table = 2
# for a in range(1, 11):
#     result = a * table
#     print(f"{table} * {a} : {result} ")

# for tableNo in range(2, 21):
#     print("\nTable : ", tableNo, "\n")
#     for a in range(1, 11):
#         result = a * tableNo
#         print(f"{tableNo} * {a} : {result} ")
#     print("\n#---------------------------#\n")



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 9. Write a function to find the first non-repeated character in a string.
def first_non_repeated_char(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

# Example usage
input_string = "swiss"
result = first_non_repeated_char(input_string)
print(f"The first non-repeated character is: {result}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
