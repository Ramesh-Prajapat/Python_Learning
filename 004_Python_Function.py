## function

"""
In Python, a function is a block of code that performs a specific task
and can be called by other parts of a program. Functions are used to
break down large programs into smaller, more manageable pieces, and to
reuse code in different parts of a program.

Here's an example of a simple function that takes two arguments and
returns their sum:
"""

# def add_numbers(a, b):
#     sum = a + b
#     return sum
#
# result = add_numbers(3, 4)
# print(result)

"""
In this example, the def keyword is used to define a function called 
add_numbers that takes two arguments, a and b. Inside the function, 
a new variable called sum is created by adding a and b. Finally, the 
return statement is used to return the value of sum to the caller.
"""

"""
Note that functions can also have default argument values, variable-length 
argument lists, and keyword arguments. Additionally, functions can modify 
global variables or have global scope themselves.
"""

## Pass by value
"""
In Python, when a function is called, arguments are passed by object reference. 
This means that a reference to the object is passed to the function, not a copy 
of the object itself.

In other words, Python uses a pass-by-object-reference model, which is different 
from the pass-by-value model used by some other programming languages like C or Java.

When a function is called with an argument in Python, the function receives a reference 
to the object, not a copy of the object. This reference can be used to modify the object, 
and any changes made to the object inside the function will affect the original object 
outside the function.

For example, consider the following code:
"""

# def increment(x):
#     x += 1
#     return x
#
# a = 10
# print(increment(a))
# print(a)


## pass by reference

"""
In Python, all function arguments are passed by object reference, which means that 
when an object is passed as an argument to a function, the function receives a reference 
to the same object, rather than a copy of the object. This is sometimes also called 
pass-by-reference.

This pass-by-reference model means that if the function modifies the object that is 
passed to it, the changes will be reflected in the original object outside the function. 
For example:
"""

# def add_one(numbers):
#     for i in range(len(numbers)):
#         numbers[i] += 1
#
# my_numbers = [1, 2, 3, 4]
# add_one(my_numbers)
# print(my_numbers)  # prints [2, 3, 4, 5]


# *args keyword
"""
In Python, the *args keyword is used to pass a variable number of arguments to a 
function. The * symbol in front of the args keyword tells Python to pack all the 
remaining positional arguments into a tuple, which can then be accessed within the function.

Here is an example of using the *args keyword:
"""

# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(sum_numbers(1, 2, 3, 4))  # prints 10
# print(sum_numbers(1, 2, 3, 4, 5))  # prints 15


"""
In this example, we define a function called sum_numbers that takes a variable 
number of arguments using the *args keyword. Inside the function, we iterate 
over all the arguments using a for loop and add them up to get the total sum. 
Finally, we return the total sum.

When we call the sum_numbers function with different numbers of arguments, 
Python automatically packs all the arguments into a tuple and passes it to the 
function through the args parameter. This allows us to pass any number of arguments 
to the function without having to explicitly define them in the function's parameter list.
"""

"""
Note that the *args keyword must be the last positional parameter in the function 
definition, since it will collect all remaining positional arguments into a tuple. 
If there are any remaining keyword arguments, they must be passed using the **kwargs 
keyword instead.
"""


## **kwargs

"""
In Python, the **kwargs keyword is used to pass a variable number of keyword arguments 
to a function. The ** symbol in front of the kwargs keyword tells Python to pack all 
the remaining keyword arguments into a dictionary, which can then be accessed within the function.

Here is an example of using the **kwargs keyword:
"""
# def print_values(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_values(name="Alice", age=30, city="New York")


"""
In this example, we define a function called print_values that takes a variable 
number of keyword arguments using the **kwargs keyword. Inside the function, we 
iterate over all the keyword arguments using a for loop and print out their key-value pairs.

When we call the print_values function with different keyword arguments, 
Python automatically packs all the keyword arguments into a dictionary and passes 
it to the function through the kwargs parameter. This allows us to pass any number of 
keyword arguments to the function without having to explicitly define them in the function's 
parameter list.
"""

"""
Note that the **kwargs keyword must be the last parameter in the function definition 
after all the positional parameters, since it will collect all remaining keyword arguments 
into a dictionary. If there are any remaining positional arguments, they must be passed using 
the *args keyword instead.
"""

"""
Also, it's important to note that the names args and kwargs are just conventions 
and can be changed to any valid variable name, although using these names can make the 
code more readable and easier to understand.
"""

## nested function
"""
In Python, a nested function is a function that is defined inside another function. 
Nested functions can be useful for encapsulating functionality and hiding it from the 
global namespace, as well as for reducing code duplication.

Here is an example of using a nested function:
"""


# def outer_function():
#     def inner_function():
#         print("This is the inner function.")
#
#     print("This is the outer function.")
#     inner_function()
#
#
# outer_function()

"""
Note that the inner function can only be called from within the outer function, 
since it is not visible in the global namespace. This can be useful for encapsulating 
functionality that should not be accessed or modified outside of the context of the outer function.
"""

## Recursion

"""
Recursion is a programming technique in which a function calls itself one or more 
times to solve a problem. Recursion is a powerful tool that can be used to solve problems 
that have a recursive structure, such as searching or traversing trees, graphs, or other data structures.

Here is an example of a recursive function in Python:
"""

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))  # prints 120


"""
In this example, we define a function called factorial that takes a number n as 
input and returns its factorial. If n is zero, the function returns 1, which is the 
base case of the recursion. Otherwise, the function multiplies n by the factorial of 
n-1, which is computed by calling the factorial function recursively with n-1 as the argument.

When we call the factorial function with an argument of 5, for example, the 
function first calls itself with an argument of 4, which in turn calls itself with 
an argument of 3, and so on, until it reaches the base case of n=0. At this point, the 
function starts returning values and multiplying them to compute the final result of 120.
"""