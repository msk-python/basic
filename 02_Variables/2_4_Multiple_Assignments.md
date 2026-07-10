# Types of Assigning Values to Variables in Python

In Python, you can assign values to variables in different ways. Below are some of the commonly used methods:

>___
>## 1. Single Value Assignment
>Assign a single value to a single variable.
>
>In this case, the variable x is assigned the integer value 10.
>
>```python
>x = 10
>```
>___


>___
>## 2. Multiple Value Assignment
>You can assign the `multiple values` to `multiple variables` in one line:
>
>```python
>x = 10
>y = 20
>z = 30
>```
>
>Here, `x` is assigned the value `10`, `y` is assigned `20`, and `z` is assigned `30`.
>
> It will assign the values `orderwise`. like: first variable is geven first value, second variable the second value and so on.
>
>### **Note:**
>
>Make sure the `number of variables` matches the `number of values`, or else you will get an `ValueError`.
>___

```py
# x, y, z = 10, 20, 30
x, y, z = 10, 20, 30, 40  # Error: too many values to unpack

print(x, y, z)
```

>However, you can collect the remaining values as a list by prefixing the variable name with an asterisk (`*`).
>
>```python
>x, y, *z = 10, 20, 30, 40, 50
>```
>
>Here, `x` is assigned `10`, `y` is assigned `20`, and `z` becomes a `list` containing `[30, 40, 50]`.
>___

```py
x, *y, z = 10, 20, 30, 70, 60
print(x, y, z)
```

>___
>## 3. Multiple Variables with the Same Value
>You can assign the `same value` to `multiple variables` in one line:
>
>```python
>x = y = z = 100
>```
>
>It will assign value `100` to all three `variables` **x**, **y**, **z**. That is, all three labels `x`, `y`, `z` will refer to same `location` with value `100`.
>___

```py
# x = 100
# y = 100
# z = 100

x = y = z = 100
print( x, y, z)
```

>___
>## 4. Unpacking a Collection
>You can assign values to variables from a collection such as a list or tuple.
>
>```python
>fruits = ["apple", "banana", "cherry"]
>x, y, z = fruits
>```
>
>In this case, `x` is assigned "apple", `y` is assigned "banana", and `z` is assigned "cherry".
>___


```py
fruits = [23, 12, 8, 9]
# print(fruits)


x , y, *z = fruits
# print(x)
print(x, y, z)
```


>___
>## 5. Dynamic Typing
>Python variables are dynamically typed, meaning you can assign different types of values to the same variable.
>
>
>Here, the variable `x` is first assigned an integer value and then reassigned with a string.
>
>___

```py
x = 50      # x is an integer
x = 'hello' # x is a string
print(x)    # hello
```


>If you want to `swap` values of **x** and **y** you just need to write:
```py
# This is wrong
x = 1
y = 2

x = y # 2
y = x # 2
print(x, y)
```


```py
x = 1
y = 2
print(x, y)

x, y = y, x
print(x, y)
```

```py
x, y = "Sumit", "Amit"

x, y = y, x
print(x , y)
```

>___
>### 3. Multiple Values in One Variable
>If you have a `collection of values` in a `tuple` etc.
```py
fruits = "apple", "banana", "Orange", 23, 45, 67
print(fruits)
```


>Python allows you to extract the values into variables. This is called **unpacking**.
```py
x , *y, z = fruits
print(x, y, z)
```