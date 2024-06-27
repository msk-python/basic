Q1: Write a program to declare and print a variable.

```py
course = "Python Basics"
print(course)
```

Q2: Write a program to declare multiple variables in a single line.

```py
a, b, c = 5, 10, 15
print(a, b, c)
```

Q3: Write a program to change the value of a variable.

```py
name = "MSK Institute"
print(name)
name = "Coding Classes"
print(name)
```

Q4: Write a program to declare a global variable inside a function.

```py
def set_global_variable():
    global institute
    institute = "MSK Institute"

set_global_variable()
print(institute)
```

Q5: Write a program to demonstrate variable scope.
```py
def my_function():
    local_var = "I'm local"
    print(local_var)

my_function()
# print(local_var)  # This will cause an error as local_var is not defined here
```

Q6: Write a program to concatenate two string variables.

```py
first_name = "MSK"
last_name = "Institute"
full_name = first_name + " " + last_name
print(full_name)
```

Q7: Write a program to increment a variable.

```py
counter = 0
counter += 1
print(counter)
```

Q8: Write a program to swap the values of two variables.

```py
a = 5
b = 10
a, b = b, a
print(a, b)
```

Q9: Write a program to declare a constant variable.

```py
PI = 3.14
print(PI)
```

Q10: Write a program to demonstrate variable assignment and reassignment.

```py
x = 10
print(x)
x = 20
print(x)
```