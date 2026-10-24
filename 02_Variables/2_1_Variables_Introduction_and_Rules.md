

>___
># Multi Words Variable Names
>Variable names with more than one word can be difficult to read.
>like this: `myvariablename`
>
>There are several techniques you can use to make them more readable:
>
>### Camel Case
>Each word, except the first, starts with a capital letter:
>
>```py
>myVariableName = "Sumit Kumar"
>```
>





>___
>### Python Variables memory references
>
>When a variable is declared and initialized in python, it will allocate memory and hold the value. This memory (along with the value) will be referenced by a variable name. Python variable is a symbolic name which is referencing to a memory.
>
>This is a sample memory block used by Python.
>
>![alt text](sample_memory_block.png)
>___

<br>

>___
>Let us understand by looking at the pictorial example,
>
>After executing the following code in python,
>
>```py
>x = 20
>y = 50
>```
>
>Two objects are created in memory which is holding the individual value.
>
>![alt text](memory_after_two_variable.png)
>
>python memory with the variable
>___


>___
>Now suppose another variable ‘p’ is created with the same value as of ‘x’, this will not create a new memory instead it will reference the memory of x with one more pointer named ‘p’.
>
>```py
>p = 20
>```
>
>![alt text](creating_third_variable.png)
>___


>___
>two equal variables in python
>
>two-variable sharing same memory
>
>When the below statement is executed,
>
>
>```py
>x = y
>```
>
>![alt text](when_x_and_y_is_equal.png)
>___


>___
>### Deleting Python Variables
>In Python, a declared variable can be deleted at any time using a del keyword. Once the variable is deleted it can not be used further in the program.
>```py
>del x
>```
>In the end, when both variables (x & p) are deleted using the python program then this memory is no more referenced (by either x or p) and at the same time, no value exists in that memory. At this point of time, the only variable y is referenced to a memory holding the value of 50.
>
>![alt text](delte_p_x_variable.png)
>___
