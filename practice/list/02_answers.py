# 1. How to find the length of "a" string?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "mskinstitute"
# print("length of the string is: ", len(s))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 2. How to reverse "a" string?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "mskinstitute"
# is_reversed =  s[::-1]
# print(f"Reversed string : ", is_reversed)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 3. How to check if a string is a palindrome.?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "madam" # racecar, level, rotor, noon, mom, wow, pop, refer, stats
# is_reversed =  s[::-1]

# if s == is_reversed:
#     print(f"Yes this is palindrome.")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 4. How to count the number of vowels in "a" string?
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


# 5. How to replace all occurrences of "world" in a string with "universe" substring.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "Hello, world! World is beautiful."
# new_s = s.replace("world", "universe")
# print(f"The new string is: {new_s}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 6. How to convert a string to uppercase and lowercase in Python?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# text = "Hello World"
# case = text.upper()
# print(case) 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 7. Write a program to remove all whitespace from a string.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# a = " This is a      string with   whitespaces. "
# result = a.replace(' ', '')
# print(result)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# 8. How can you check if a string contains only alphabets in Python?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# string = "HelloWorld"
# # string = "HelloWorld123"
# print(string.isalpha())
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# 9. How to find the first non-repeated character in a string.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# s = "swiss"

# for char in s:
#     if s.count(char) == 1:
#         print(f"The first non-repeated character is: {char}")
#         break
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 10. How to split a string into a list of words?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# text = "Hello world this is a string"

# word_list = text.split()
# print(word_list)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 11. How can you remove a specific character from a string in Python?
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# text = "Hello, World!"
# char_to_remove = "!"
# modified_string = text.replace(char_to_remove, "")
# print(modified_string)  # Output: Hello World!
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 12. Write a function to check if a string starts with a specified prefix and ends with a specified suffix.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def starts_with_prefix_ends_with_suffix(string, prefix, suffix):
#     return string.startswith(prefix) and string.endswith(suffix)

# # Example usage:
# text = "HelloWorld"
# start = "Hello"
# end = "World"
# print(starts_with_prefix_ends_with_suffix(text, start, end))  # Output: True
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#---------------- Print only-one table ----------------------#
# table = 2
# for a in range(1, 11):
#     result = a * table
#     print(f"{table} * {a} : {result} ")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# for tableNo in range(2, 21):
#     print("\nTable : ", tableNo, "\n")
#     for a in range(1, 11):
#         result = a * tableNo
#         print(f"{tableNo} * {a} : {result} ")
#     print("\n#---------------------------#\n")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>