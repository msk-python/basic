# 1	    What is Python, and why is it widely used in programming?
# Ans: 

# 2	    How do you install Python and set up the Python environment on your system?

# 3	    Explain the importance of indentation in Python. Provide an example.
# 4	    How can you write single-line and multi-line comments in Python?
# 5	    How do you declare and assign values to variables in Python? Provide an example.
# 6	    What are the different data types in Python? Name at least five with examples.
# 7	    Explain the difference between integers and floating-point numbers in Python.
# 8	    How can you convert a float to an integer in Python? Provide an example.
# 9	    What are the different types of operators in Python? Provide examples of arithmetic, comparison, and logical operators.
# 10	How can you concatenate two strings in Python? Provide an example.
# 11	How do you create a list in Python, and how can you add an element to it?
# 12	What is a tuple in Python, and how is it different from a list? Provide an example.
# 13	What is a set in Python, and how do you add elements to a set?
# 14	How do you create a dictionary in Python, and how can you access an element using a key?
# 15	How do conditional statements work in Python? Provide an example of an if-elif-else statement.
# 16	What is the difference between a for loop and a while loop in Python? Provide examples of each.
# 17	How do you define a function in Python, and how do you call it? Provide an example.
# 18	How can you check the type of a variable in Python? Provide an example.
# 19	What is the result of dividing 10 by 3 in Python? How can you get both the quotient and remainder?
# 20	How do you use the modulo operator (%) in Python? Provide an example.


























# Q1 reverse items given in this example:
a = [ 1, 3, 5, 2, 6 ]           # answer: [ 6, 2, 5, 3, 1 ]



    
    
# Q2 how to get power of given n value
#   4^8                     answer: 65,536


# Q3 sum to all numbers given in list.
# a = [ 66, 77, 88, 99 ]    # answer: 330


# Q4 sum all int numbers
# a = [ 2,  4 , 23.5, 5.6, 6 ]


# Q5 sum all int numbers & float 
a = [ 2,  4 , 23.5, 5.6, 6 ]







# a = 9
# # a = None
# del a
# print( a )


def power_of(power_of, power):
    return power_of ** power

# print(  power_of( 4, 8 ) )

def sum_all( list ):
    result = 0
    for n in list:
        result += n
    return result

# print(  sum_all( a ) )








#   a[::-1]






def sum_int( list ):
    result = 0
    for n in list:
        if isinstance( n, int ):
            result += n
    return result

# print( sum_int( a ) )







a = [ 2,  4 , 23.5, 5.6, 6 ]

def sum_int_float( list ):
    int_result = 0
    float_result = 0
    for n in list:
        if isinstance( n, int ):
            int_result += n
        if isinstance( n, float ):
            float_result += n
    
    result = f"Float Result: {float_result} \nInt Result : {int_result} "
    return result

print( sum_int_float( a ) )
