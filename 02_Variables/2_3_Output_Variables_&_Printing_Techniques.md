# Output Variables
The Python `print()` function is often used to `output` variables.

```py
x = "Python is awesome"
print(x)
```

In the `print()` function, you output multiple variables, separated by a `comma (,)`:

```py
x = "Python"
y = 12
z = "awesome"

print(x , y , z)
```

You can also use the `(+)` operator to output multiple variables:

```py
x = "Python"
y = "is"
z = "awesome"
print(x + y + z)
```

Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

For numbers, the `(+)` character works as a `mathematical operator`:

```py
x = 5
y = 10

print(x + y)
print(x , y)
```


In the `print()` function, when you try to `combine` a `string` and a `number` with the `(+)` operator, Python will give you an `error`:

```py
x = 5
y = "Sumit"

print(x + y) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Note: The `best way` to output multiple variables in the `print()` function is to separate them with commas `(,)`, which even support `different data` types:

```py
x = 5
y = "Computer"
print(x , y)
```
