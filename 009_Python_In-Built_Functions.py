## abs()
"""
In Python, abs() is a built-in function that returns the absolute
value of a number. The absolute value of a number is its distance
from zero on the number line, regardless of whether the number is
positive or negative.

Note that the abs() function can be used with integers, floating-
point numbers, and complex numbers. When used with complex numbers,
abs() returns the magnitude of the complex number, which is the
distance from the origin in the complex plane.

Overall, the abs() function is a useful tool for working with numbers
in Python, especially when you need to calculate distances or differences
between numeric values.
"""
# print(abs(5))         # returns 5
# print(abs(-5))        # returns 5
# print(abs(3.141592))  # returns 3.141592
# print(abs(-3.141592)) # returns 3.141592




## all()
"""
In Python, all() is a built-in function that returns True if 
all the elements of an iterable are true (or if the iterable 
is empty), and False otherwise.
Syntax:- all(iterable)
"""
# print(all([True, True, True]))     # returns True
# print(all([True, False, True]))    # returns False
# print(all([]))                     # returns True
# print(all((2, 4, 6, 8)))          # returns True
# print(all([x > 0 for x in [1, 2, 3]])) # returns True




## any()
"""
In Python, any() is a built-in function that returns True if any 
element of an iterable is true, and False otherwise. If the iterable 
is empty, any() returns False.
syntax:- any(iterable)
"""

# print(any([True, True, True]))     # returns True
# print(any([True, False, True]))    # returns True
# print(any([]))                     # returns False
# print(any((0, 0, 0, 1)))          # returns True
# print(any([x > 0 for x in [1, 2, 3]])) # returns True




## bin()
"""
In Python, the bin() function is used to convert an integer 
number to its binary string representation. The function 
takes an integer as an argument and returns a string that 
represents the binary equivalent of the input integer.

Here's the syntax of the bin() function:
bin(number)
"""

# print(bin(5))
#
# print("{0:b}".format(5))
#In this example, the format() method is used to convert the integer
# 5 to binary. The :b format specifier is used to indicate that the integer
# should be formatted as a binary string.




## bool(value)
"""
In Python, the bool() function is used to convert a value to a boolean. 
It returns either True or False depending on the input value.

Here's the syntax of the bool() function:
bool(value)
"""
# print(bool(1))
# print(bool(0))

"""
Note that in Python, some values are considered False when converted 
to boolean, while others are considered True. Here's a list of values 
that are considered False:
1. False
2. None
3. 0 (integer)
4. 0.0 (float)
5. "" (empty string)
6. [] (empty list)
7. {} (empty dictionary)
8. set() (empty set)
"""




## breakpoint()
"""
The breakpoint() function is a built-in function in Python 3.7 and
later versions that can be used for debugging purposes. It provides 
a way to pause the execution of a program and enter into the debugger 
at a specific point in the code.

Here's the syntax of the breakpoint() function:
breakpoint(*args, **kwargs)
"""
# def add_numbers(a, b):
#     breakpoint()
#     result = a + b
#     return result
#
# add_numbers(2, 3)

"""
When the breakpoint() function is called, it raises a BdbQuit 
exception, which is caught by the Python debugger. This allows 
the debugger to take control and pause the program at the point 
where the breakpoint() function was called.
"""




## bytearray()
"""
In Python, bytearray() is a built-in function that creates a 
mutable array of bytes from a sequence of integers or bytes. The 
function returns a bytearray object, which is similar to a list 
but can only contain integers between 0 and 255.
"""

# bytes = bytearray([65, 66, 67, 68])
# print(bytes)
#
# string = "Ramesh Prajapat"
# bytes = bytearray(string, 'utf-8')
# print(bytes)

"""
In the above examples, a bytearray is created from a sequence 
of integers, a string, and modified by changing a byte value. 
The bytearrays can also be concatenated with the += operator. 
Note that the b prefix in the print() statements indicates that 
the output is a bytearray.
"""




## bytes()
"""
In Python, bytes() is a built-in function that creates an 
immutable array of bytes from a sequence of integers or bytes. 
The function returns a bytes object, which is similar to a 
bytearray but is immutable.
"""




## callable()
"""
In Python, callable() is a built-in function that determines 
whether an object is callable or not. A callable object is an 
object that can be called like a function, using parentheses 
and arguments.

The callable() function is often used in combination with error 
handling to ensure that a given object is callable before attempting 
to call it. This can help prevent errors and improve the robustness 
of the code.
"""
# Define a function and a class
# def my_function():
#     pass
#
# class MyClass:
#     def __call__(self):
#         pass
#
# print(callable(my_function)) # Return True
# obj = MyClass()
# print(callable(obj)) # return True
#
# x = 123
# print(callable(x)) # return False




## chr()
"""
In Python, chr() is a built-in function that returns the string 
representation of a Unicode character that matches the specified 
Unicode code point (integer).

Here's the syntax of the chr() function:
chr(i)

It is important to note that chr() can only convert code points within 
the range of 0 to 1,114,111 (0x10FFFF) inclusive, which is the range 
of Unicode code points. Any integer outside this range will raise a 
ValueError.
"""

# print(chr(65))
# print(chr(8364))
# print(chr(128169))




## classmethod()
"""
In Python, classmethod() is a built-in function that creates a class 
method from a regular method. A class method is a method that is bound 
to the class and not the instance of the class. Class methods are often 
used to create alternative constructors for a class or to modify class-level 
attributes.
"""

# class MyClass:
#     class_attr = 0
#
#     def __init__(self, instance_attr):
#         self.instance_attr = instance_attr
#
#     def instance_method(self):
#         print("Instance method called")
#
#     @classmethod
#     def class_method(cls):
#         print("Class method called")
#         cls.class_attr += 1

# # Call the class method
# MyClass.class_method()
#
# # Access the class-level attribute
# print(MyClass.class_attr)
#
# # Create an instance of the class
# obj = MyClass("Instance attribute")
#
# # Call the instance method
# obj.instance_method()
#
# # Cannot access class-level attribute from the instance
# print(obj.class_attr) # Error




## delattr()
"""
In Python, the delattr() function is a built-in function that is used 
to delete an attribute from an object. The delattr() function takes 
two arguments: the object from which the attribute should be deleted, 
and the name of the attribute to be deleted.

Here's the syntax of the delattr() function:
delattr(obj, name)

where obj is the object from which the attribute should be deleted, 
and name is the name of the attribute to be deleted.

Note that the delattr() function can be useful in situations where 
you need to remove an attribute from an object dynamically at runtime.
"""
# Define a simple class with two attributes
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# # Create a Person object
# p = Person("Alice", 30)
#
# # Delete the age attribute from the Person object
# delattr(p, "age")




## dict()
"""
In Python, the dict() function is a built-in function that creates 
a new dictionary object. A dictionary is an unordered collection of 
key-value pairs, where each key is unique and maps to a corresponding 
value.

The dict() function can be useful in a variety of situations where you 
need to create a dictionary object, such as when reading data from a 
file or database, or when parsing JSON or other structured data formats.
"""

# The dict() function can be called in three different ways:
"""
1. With keyword arguments: 
        In this case, the keys and values of the new dictionary are 
        specified as keyword arguments. For example:
"""
# # Create a dictionary using keyword arguments
# d1 = dict(a=1, b=2, c=3)
#
# # Print the dictionary
# print(d1)   # {'a': 1, 'b': 2, 'c': 3}

"""
2. With a mapping object: 
        In this case, the keys and values of the new dictionary are 
        taken from the items of the mapping object. For example:
"""
# # Create a dictionary using a mapping object
# d2 = dict({'a': 1, 'b': 2, 'c': 3})
#
# # Print the dictionary
# print(d2)   # {'a': 1, 'b': 2, 'c': 3}

"""
3. With an iterable of key-value pairs: 
        In this case, the keys and values of the new dictionary are 
        taken from the items of the iterable. For example:
"""

# # Create a dictionary using an iterable of key-value pairs
# d3 = dict([('a', 1), ('b', 2), ('c', 3)])
#
# # Print the dictionary
# print(d3)   # {'a': 1, 'b': 2, 'c': 3}




## dir()
"""
In Python, the dir() function is a built-in function that returns a 
list of the names of the attributes and methods of an object. If the 
object passed to dir() is not specified, it returns the list of names 
in the current scope.

The dir() function can be useful for exploring the attributes and 
methods of an object, especially when working with unfamiliar libraries or modules.
"""
# Define a simple class
# class MyClass:
#     def __init__(self):
#         self.x = 1
#         self.y = 2
#
#     def my_method(self):
#         print("Hello, world!")
#
#
# # Create an instance of the class
# my_obj = MyClass()
#
# # Call the dir() function on the object
# print(dir(my_obj))




## divmod()
"""
In Python, the divmod() function is a built-in function that takes two 
arguments and returns a tuple containing the quotient and remainder of 
dividing the first argument by the second argument. The first argument 
is the dividend and the second argument is the divisor.

Here's the syntax of the divmod() function:
divmod(a, b)

The divmod() function takes two arguments a and b and returns a tuple 
containing two values: the quotient of a divided by b, and the remainder 
of a divided by b.

The divmod() function can be useful in a variety of situations where 
you need to perform division and also need the remainder. For example, 
when working with time values, you might use divmod() to calculate the 
number of hours, minutes, and seconds in a given number of seconds.
"""
# # Calculate the quotient and remainder of dividing 20 by 3
# result = divmod(20, 3)
#
# # Print the result
# print(result)   # (6, 2)




## enumerate()
"""
In Python, the enumerate() function is a built-in function that adds a 
counter to an iterable and returns an enumerated object. The enumerated 
object contains pairs of the form (index, item) for each item in the 
original iterable.

Here's the syntax of the enumerate() function:
enumerate(iterable, start=0)

The enumerate() function is often used in situations where you need to 
keep track of the index or position of items in an iterable. It can be 
especially useful when working with loops and conditional statements.
"""
# # Create a list of fruits
# fruits = ['apple', 'banana', 'cherry']
#
# # Enumerate the list of fruits
# for index, fruit in enumerate(fruits):
#     print(index, fruit)




## exec()
"""
In Python, the exec() function is a built-in function that executes a 
string as a Python program and returns None. The string can contain 
any valid Python code, including variable assignments, function definitions, 
and conditional statements.
"""
# # Define a function using exec()
# func_str = "def my_function(x): return x**2"
# exec(func_str)
#
# # Call the function
# result = my_function(5)
# print(result)   # 25

# # Execute a more complex program using exec()
# prog_str = """
# for i in range(10):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")
# """
# exec(prog_str)




## filter()
"""
The filter() function in Python is a built-in function that allows you 
to filter out elements from a sequence (e.g., list, tuple, or string) 
based on a given condition.

The syntax for the filter() function is as follows:
filter(function, iterable)


"""
# # define a list of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # define a lambda function that checks if a number is even
# is_even = lambda x: x % 2 == 0
#
# # use the filter() function to filter out the even numbers from the list
# even_numbers = list(filter(is_even, numbers))
#
# # print the filtered list
# print(even_numbers)   # Output: [2, 4, 6, 8, 10]




## float()
"""
The float() function in Python is a built-in function that converts a 
string or a number to a floating-point number.
"""
# converting a string to a float
# my_string = "3.14"
# my_float = float(my_string)
# print(my_float)   # Output: 3.14




## format()
"""
The format() function in Python is a built-in function that allows you 
to format a string by replacing placeholders with values. The format() 
function takes one or more arguments, which can be either positional 
or keyword arguments, and returns a formatted string.

The syntax for the format() function is as follows:
formatted_string = format(template_string, *args, **kwargs)
"""

# Here are some examples of how to use the format() function:
# Using positional arguments:

# # 1. using positional arguments to format a string
# template_string = "Hello, Today is {}."
# formatted_string = template_string.format("Monday")
# print(formatted_string)   # Output: Hello, Today is Monday.


# # 2. using keyword arguments to format a string
# template_string = "Hello, {name}! Today is {day}."
# formatted_string = template_string.format(name="Bob", day="Tuesday")
# print(formatted_string)   # Output: Hello, Bob! Today is Tuesday.

# 3. Using placeholders with format specifiers:# using placeholders with format specifiers to format a string
# template_string = "The value of pi is approximately {:.2f}."
# formatted_string = template_string.format(3.14159)
# print(formatted_string)   # Output: The value of pi is approximately 3.14.




## frozenset()
"""
The frozenset() function in Python is a built-in function that returns 
an immutable frozenset object. A frozenset is a set that cannot be modified 
once it is created, and it is hashable, which means it can be used as a key 
in a dictionary.

The syntax for the frozenset() function is as follows:
frozen_set = frozenset(iterable)

Note that since frozensets are immutable, they cannot be modified after 
they are created. Therefore, methods that modify sets, such as add(), 
remove(), and clear(), are not available for frozensets. However, frozensets 
can be used in many of the same ways as regular sets, such as performing set 
operations like union, intersection, and difference.
"""

# 1. Creating a frozedset from a list:
# creating a frozenset from a list
# my_list = [1, 2, 3]
# my_frozenset = frozenset(my_list)
# print(my_frozenset)   # Output: frozenset({1, 2, 3})

# 2. Creating a frozenset from a string
# creating a frozenset from a string
# my_string = "hello"
# my_frozenset = frozenset(my_string)
# print(my_frozenset)   # Output: frozenset({'h', 'o', 'e', 'l'})




## getattr()
"""
The getattr() function in Python is a built-in function that is used 
to retrieve the value of a named attribute from an object. The getattr() 
function takes two arguments:

1. object: 
        The object from which you want to retrieve the attribute.
2. name: 
        A string representing the name of the attribute that you want 
        to retrieve.
"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person = Person("Alice", 25)
#
# # Using dot notation to access the name attribute
# print(person.name)  # Output: "Alice"
#
# # Using getattr() to access the name attribute
# print(getattr(person, "name"))  # Output: "Alice"
#
# # Using getattr() to access a non-existent attribute
# print(getattr(person, "height", "Unknown"))  # Output: "Unknown"




## hasattr()
"""
The hasattr() function in Python is a built-in function that is used 
to check whether an object has a named attribute or not. The hasattr() 
function takes two arguments:

1. object: 
        The object that you want to check for the named attribute.
2. name: 
        A string representing the name of the attribute that you want to 
check for.

 The hasattr() function is often used in combination with getattr() to 
 check for the presence of an attribute before attempting to retrieve 
 its value.
"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person = Person("Alice", 25)
#
# # Using hasattr() to check for the name attribute
# if hasattr(person, "name"):
#     print("person has a name attribute")
#
# # Using hasattr() to check for a non-existent attribute
# if not hasattr(person, "height"):
#     print("person does not have a height attribute")




## hash()
"""
The hash() function in Python is a built-in function that returns the 
hash value of an object. A hash value is a fixed-size integer that 
represents a unique value for the object being hashed.

Here is an example usage of hash():

The hash() function can be used to hash immutable objects such as strings, 
numbers, and tuples. However, mutable objects such as lists and dictionaries 
cannot be hashed, as their values can change over time. If you attempt to 
hash a mutable object, a TypeError will be raised.

It is worth noting that the hash value returned by hash() can be used as 
a key in a dictionary or as an element in a set. This is because hash values 
are unique and can be used to identify objects. In fact, the dict and set 
data types in Python use hash values internally to store and retrieve values 
efficiently.
"""

# hash_value = hash("Hello World")
# print(hash_value)




## help()
"""
The help() function in Python is a built-in function that provides a 
help message about a specified object. It can be used to get information 
about built-in Python objects, as well as user-defined functions, modules, 
classes, and methods.

In addition to providing help messages, the help() function can also be
 used to generate documentation for modules and packages. This is typically 
 done by adding docstrings to the module or package, and then running the 
 help() function on the module or package name.

Here is an example usage of help():
"""

# Help for a user-defined function
# def my_function(x):
#     """
#     A simple function that squares its input.
#     """
#     return x**2
#
# help(my_function)




## hex()

"""
The hex() function in Python is a built-in function that converts an 
integer to a hexadecimal string. The returned string starts with the 
prefix '0x' to indicate that it is a hexadecimal value.
"""
# # Convert an integer to a hexadecimal string
# hex_value = hex(65)
# print(hex_value)




## id()
"""
The id() function in Python is a built-in function that returns the 
unique identifier (integer) for a specified object. This identifier 
is guaranteed to be unique and constant for the lifetime of the object, 
and can be used to compare two objects for identity.

Here is an example usage of id():
"""

# # Create a list object and get its identifier
# my_list = [1, 2, 3]
# print(id(my_list))

"""
The id() function can be used with any Python object, including built-in 
objects like integers, floats, and strings, as well as user-defined 
objects like classes and instances.
"""
# # Get the identifier of a string object
# my_string = "Hello, world!"
# print(id(my_string))
"""
It is important to note that the id() function does not guarantee that 
the memory location of an object will remain constant across different 
executions of a Python program. In other words, the same object may have 
a different identifier in different runs of the program. However, within 
a single run of a program, the id() function provides a reliable way to 
compare objects for identity
"""




## input()
"""
The input() function in Python is a built-in function that allows a user 
to enter data through the keyboard while a program is running. It reads 
a line of text from the user and returns it as a string.

It is important to note that the input() function always returns a string, 
even if the user enters a number or other type of input. Therefore, if you 
need to perform calculations or comparisons with the input, you may need to 
convert it to a different data type using functions like int(), float(), or 
bool().

Here is an example usage of input():
"""
# # Ask the user for their name and print a greeting
# name = input("What is your name? ")
# print("Hello, " + name + "!")




## int()
"""
The int() function in Python is a built-in function that converts a 
specified value into an integer. It can be used to convert a string 
or a float to an integer.

Here are some examples of using the int() function:
"""
# # Convert a string to an integer
# num_str = "123"
# num_int = int(num_str)
# print(num_int)




## isinstance()
"""
The isinstance() function in Python is a built-in function that is used 
to check if an object is an instance of a specified class or subclass
Syntax:- isinstance(object, classinfo)

object: The object that you want to check.
classinfo: The class or tuple of classes that you want to check against.

The function returns True if the object is an instance of the specified 
class or subclass, and False otherwise.


The isinstance() function is commonly used in object-oriented programming 
to check the type of an object before performing operations on it, or to 
determine the type of an object returned by a function or method.
"""
# # Check if an object is an integer
# num = 123
# if isinstance(num, int):
#     print("num is an integer")
# else:
#     print("num is not an integer")
#
# # Check if an object is a string or a list
# text = "Hello, world!"
# if isinstance(text, (str, list)):
#     print("text is a string or a list")
# else:
#     print("text is not a string or a list")




## issubclass()
"""
The issubclass() function in Python is a built-in function that is used 
to check if a class is a subclass of another class or a tuple of classes.

syntax: issubclass(class, classinfo)

class: The class that you want to check.
classinfo: The class or tuple of classes that you want to check against.

The function returns True if the class argument is a subclass of any of 
the classes specified in classinfo, and False otherwise.


The issubclass() function is commonly used in object-oriented programming 
to check the inheritance relationships between classes.
"""

# Check if a class is a subclass of another class
class Animal:
    pass

# class Dog(Animal):
#     pass
#
# if issubclass(Dog, Animal):
#     print("Dog is a subclass of Animal")
# else:
#     print("Dog is not a subclass of Animal")




## iter()
"""
The iter() function in Python is a built-in function that returns an 
iterator object for a given iterable.

Here is the syntax for using the iter() function:
iter(iterable, sentinel)

iterable: 
    The iterable object for which to create an iterator.
sentinel (optional): 
    A value that is used to signal the end of the iteration. If this 
    argument is not provided, the iterable object must be an object that 
    supports the iterator protocol.

The iter() function returns an iterator object that can be used to iterate 
over the elements of the iterable object. The sentinel argument, if 
provided, is used to signal the end of the iteration. If the sentinel 
argument is not provided, the iterator will continue indefinitely until 
the iterable object is exhausted.

The iter() function is commonly used in Python to create iterator objects 
for iterables such as lists, tuples, dictionaries, sets, and files.
"""

# # Create an iterator object for a list
# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)
#
# # Iterate over the elements of the list using the iterator
# for i in my_iterator:
#     print(i)




## len()
"""
In Python, len() is a built-in function that returns the length 
(number of items) of an object. It can be used with a variety of 
data types such as strings, lists, tuples, sets, and dictionaries.

Here is the syntax for using the len() function:
len(object)
"""

# # Example 1 - Finding the length of a string
# my_string = "Hello, World!"
# print(len(my_string))  # Output: 13
#
# # Example 2 - Finding the length of a list
# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))  # Output: 5
#
# # Example 3 - Finding the length of a dictionary
# my_dict = {"name": "John", "age": 30, "city": "New York"}
# print(len(my_dict))  # Output: 3




## list()
"""
In Python, list() is a built-in function that creates a new list object. 
It can be used to create an empty list or to convert an iterable (such 
as a tuple or a string) into a list.

Here is the syntax for using the list() function:
"""
# # Example 1 - Creating an empty list
# my_list = list()
# print(my_list)  # Output: []
#
# # Example 2 - Converting a tuple into a list
# my_tuple = (1, 2, 3, 4, 5)
# my_list = list(my_tuple)
# print(my_list)  # Output: [1, 2, 3, 4, 5]
#
# # Example 3 - Converting a string into a list
# my_string = "Hello, World!"
# my_list = list(my_string)
# print(my_list)  # Output: ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']




## locals()
"""
In Python, locals() is a built-in function that returns a dictionary 
containing the current local symbol table. The local symbol table 
contains information about the variables and their values that are 
currently in scope in the current function or module.

Here is the syntax for using the locals() function:
locals()

The locals() function can be useful for debugging and introspection 
purposes, as it allows you to inspect the local variables and their 
values in a function. However, it's important to note that the locals() 
function only returns information about the local symbol table in the 
current scope, so it won't provide information about variables in other 
scopes (such as global variables).
"""

# def my_function():
#     x = 1
#     y = 2
#     print(locals())
#
# my_function()




## map()
"""
In Python, map() is a built-in function that applies a given function 
to each item of an iterable (such as a list, tuple, or string) and 
returns a new iterable containing the results. The map() function is 
an example of a higher-order function, which means that it takes another 
function as an argument.

Here is the syntax for using the map() function:
map(function, iterable)

"""
# # Example 1 - Squaring each item in a list
# my_list = [1, 2, 3, 4, 5]
# squared_list = list(map(lambda x: x**2, my_list))
# print(squared_list)  # Output: [1, 4, 9, 16, 25]
#
# # Example 2 - Converting each string in a list to uppercase
# my_strings = ["hello", "world", "python"]
# uppercase_strings = list(map(str.upper, my_strings))
# print(uppercase_strings)  # Output: ['HELLO', 'WORLD', 'PYTHON']




## max()
"""
In Python, max() is a built-in function that returns the largest item in 
an iterable or the largest of two or more arguments. The max() function 
can be used with a variety of different data types, including lists, 
tuples, and strings.

Here is the syntax for using the max() function:
max(iterable, *iterables, key=None, default=None)
"""

# # Example 1 - Finding the maximum value in a list
# my_list = [1, 2, 3, 4, 5]
# max_value = max(my_list)
# print(max_value)  # Output: 5
#
# # Example 2 - Finding the maximum value in a tuple
# my_tuple = (10, 20, 30, 40, 50)
# max_value = max(my_tuple)
# print(max_value)  # Output: 50
#
# # Example 3 - Finding the maximum value in a string
# my_string = "Hello, world!"
# max_value = max(my_string)
# print(max_value)  # Output: 'w'




## min()
"""
In Python, min() is a built-in function that returns the smallest item 
in an iterable or the smallest of two or more arguments. The min() 
function can be used with a variety of different data types, including 
lists, tuples, and strings.

Here is the syntax for using the min() function:
"""
# # Example 1 - Finding the minimum value in a list
# my_list = [5, 2, 8, 1, 3]
# min_value = min(my_list)
# print(min_value)  # Output: 1
#
# # Example 2 - Finding the minimum value in a tuple
# my_tuple = (50, 40, 30, 20, 10)
# min_value = min(my_tuple)
# print(min_value)  # Output: 10
#
# # Example 3 - Finding the minimum value in a string
# my_string = "Hello, world!"
# min_value = min(my_string)
# print(min_value)  # Output: ' '




## next()
"""
In Python, next() is a built-in function used to retrieve the next 
item from an iterator. An iterator is an object that allows you to 
iterate over a collection of values, such as a list or a tuple.

The next() function takes an iterator object as its argument and returns 
the next item in the sequence. If there are no more items in the sequence, 
it raises the StopIteration exception.
"""
# numbers = iter([1, 2, 3, 4, 5])
#
# print(next(numbers))  # Output: 1
# print(next(numbers))  # Output: 2
# print(next(numbers))  # Output: 3
# print(next(numbers))  # Output: 4
# print(next(numbers))  # Output: 5
# print(next(numbers))  # Raises StopIteration exception




## object()
"""
In Python, the object() function is a built-in function that returns a 
new empty object. This function is rarely used in practice, as it is 
typically used as a base class for other classes to inherit from.
"""
# class MyClass(object):
#     pass
#
# my_object = MyClass()

"""
In this example, we define a new class called MyClass that inherits from 
the object class using the parentheses (). This is equivalent to writing 
class MyClass: because object is the default base class if none is 
provided explicitly. We then create an instance of this class using the 
MyClass() syntax, which creates a new object of the MyClass class.

Note that in Python 3, the parentheses are optional when inheriting from 
object, so we can also define the class like this:


class MyClass:
    pass

"""




## oct()
"""
In Python, the oct() function is a built-in function that returns the 
octal (base 8) representation of an integer. The function takes an 
integer as its argument and returns a string representing the octal 
value of the integer.

"""
# decimal_number = 123
# octal_number = oct(decimal_number)
# print(octal_number)  # Output: '0o173'

"""
In this example, we pass an integer 123 as an argument to the oct() 
function. The function returns a string '0o173' that represents the 
octal value of the integer. The prefix '0o' indicates that the number 
is in octal format.

The oct() function can also take a negative integer as an argument. In 
this case, the octal representation of the negative integer is returned 
with a leading '-' character. Here is an example:
"""




## open()
"""
In Python, the open() function is a built-in function used for opening a 
file in a specified mode. The function returns a file object, which can 
be used to read or write data to the file.

syntax:
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
"""




## ord()
"""
In Python, the ord() function is a built-in function that returns the 
Unicode code point (integer representation) of a specified character.

The ord() function takes a single character string as its argument, and 
returns an integer that represents the Unicode code point of that 
character.
"""
# character = 'A'
# unicode_code_point = ord(character)
# print(unicode_code_point)  # Output: 65




## pow()
"""
In Python, the pow() function is a built-in function that returns the 
result of raising a number to a specified power.

The pow() function takes two or three arguments, depending on whether you 
want to compute a simple power or a modular exponentiation:

If you pass two arguments, pow(x, y) returns the value of x raised to the 
power of y.

If you pass three arguments, pow(x, y, z) returns (x**y) % z, which is the 
result of raising x to the power of y modulo z.
"""
# # Simple power
# result = pow(2, 3)  # 2 raised to the power of 3
# print(result)       # Output: 8
#
# # Modular exponentiation
# result = pow(2, 3, 5)  # 2 raised to the power of 3, modulo 5
# print(result)          # Output: 3




## print()
"""
In Python, the print() function is a built-in function that allows you 
to output text and other data to the console or other output streams.

The print() function takes one or more arguments, separated by commas. 
It converts each argument to a string and concatenates them together, 
with a space character between each one. It then outputs the resulting 
string to the console.
"""

# print("Hello , world!")
# #You can also specify a separator between the arguments by using the sep parameter:
# print("1", "2", "3", "4", "5", sep=", ")  # Output: 1, 2, 3, 4, 5




## property()
"""
In Python, the property() function is a built-in function that allows you 
to define a special kind of attribute called a "property" on a class.

A property is an attribute that is accessed like a regular attribute, but 
when it is accessed, a method associated with the property is called to 
compute the value of the attribute dynamically. This allows you to define 
custom behavior for getting, setting, and deleting attributes of an object.

The property() function takes up to four arguments, which are all optional:

1. fget: A function that will be called when the property is accessed.
2. fset: A function that will be called when the property is assigned a new value.
3. fdel: A function that will be called when the property is deleted.
4. doc: A string that will be used as the property's docstring.
"""

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         if value <= 0:
#             raise ValueError("Width must be positive.")
#         self._width = value
#
#     @property
#     def height(self):
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         if value <= 0:
#             raise ValueError("Height must be positive.")
#         self._height = value
#
#     @property
#     def area(self):
#         return self._width * self._height
#
# r = Rectangle(3, 4)
# print(r.width)   # Output: 3
# print(r.height)  # Output: 4
# print(r.area)    # Output: 12




## set()
"""
In Python, the set() function is a built-in function that creates a new 
set object. A set is an unordered collection of unique elements.

You can create a set by passing an iterable object (e.g. a list, tuple, 
or string) to the set() function. The function will remove any duplicate 
elements from the iterable and create a new set object containing the 
unique elements.

Here are some examples of how to use the set() function:
"""
# numbers = [1, 2, 3, 2, 1, 4, 5, 4]
# unique_numbers = set(numbers)
# print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
#
# letters = "hello world"
# unique_letters = set(letters)
# print(unique_letters)  # Output: {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}




## setattr()
"""
In Python, the setattr() function is a built-in function that sets the 
value of an attribute on an object.

The setattr() function takes three arguments:

    object: The object on which to set the attribute.
    name: The name of the attribute to set.
    value: The value to set the attribute to.


Here's an example of how to use the setattr() function:
"""

# class Person:
#     pass
#
# person = Person()
# setattr(person, 'name', 'John')
# print(person.name)  # Output: John

"""
Note that while the setattr() function is a powerful tool for dynamic 
attribute setting, it should be used judiciously and with care to avoid 
unintended consequences or security vulnerabilities.
"""

# my_list = []
# setattr(my_list, 'my_attribute', 'Hello')
# print(my_list.my_attribute)  # Output: Hello
#
# my_dict = {}
# setattr(my_dict, 'my_key', 'World')
# print(my_dict['my_key'])  # Output: World




## slice()
"""
In Python, the slice() function returns a slice object that can be used 
to slice a sequence, such as a string, list, or tuple.

A slice object is created using the slice() function and specifies the 
start, stop, and step values for a slice operation. The start value is 
the index where the slice starts (inclusive), the stop value is the index 
where the slice ends (exclusive), and the step value is the number of 
indices to skip between items in the slice.
"""

# my_list = [1, 2, 3, 4, 5]
# my_slice = slice(1, 4, 2)
# print(my_list[my_slice])  # Output: [2, 4]

"""
In this example, we create a list my_list that contains five elements. 
We then create a slice object my_slice using the slice() function with a 
start value of 1, a stop value of 4, and a step value of 2. We then use 
the slice object to slice the my_list object, which returns a new list 
containing only the elements at indices 1 and 3 (2 and 4).
"""

#You can also use slice objects directly in slice notation, like this:
# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4:2])  # Output: [2, 4]




## sorted()
"""
In Python, the sorted() function is a built-in function that returns a sorted 
list from the items in an iterable.

The sorted() function takes one mandatory argument, which is the iterable 
to be sorted. Optionally, you can also provide two keyword arguments: key 
and reverse. The key argument is a function that takes an element of the 
iterable as input and returns a value to use for sorting. The reverse 
argument is a boolean value that indicates whether to sort the iterable 
in reverse order (True) or in ascending order (False, which is the default).
"""
# my_list = [3, 2, 1, 4, 5]
# sorted_list = sorted(my_list)
# print(sorted_list)  # Output: [1, 2, 3, 4, 5]

#You can also use the key and reverse arguments to sort the iterable in different ways.
# my_list = ['apple', 'banana', 'orange', 'pear']
# sorted_list = sorted(my_list, key=lambda x: len(x), reverse=True)
# print(sorted_list)  # Output: ['banana', 'orange', 'apple', 'pear']

"""
In this example, we create a list my_list that contains four strings. We 
then use the sorted() function with a key function that returns the length 
of each string and a reverse argument set to True to create a new list 
sorted_list that contains the strings in my_list sorted by length in 
descending order. We then print the sorted list to verify that it has 
been sorted correctly.

Note that while the sorted() function is a powerful tool for sorting iterables, 
it creates a new list and does not modify the original iterable. If you 
want to sort the original iterable in place, you can use the sort() method 
of the iterable object.
"""




## staticmethod()
"""
In Python, the staticmethod() function is a built-in function that returns 
a static method object from a function. A static method is a method that 
belongs to a class rather than an instance of the class, and does not receive 
an implicit first argument (self).

To create a static method, you can use the staticmethod() function to decorate 
a function definition inside a class:
"""
# class MyClass:
#     @staticmethod
#     def my_static_method(arg1, arg2):
#         return arg1 + arg2

"""
In this example, we define a static method my_static_method inside a class 
MyClass. The static method takes two arguments, arg1 and arg2, and simply 
returns their sum. Note that the static method does not receive an implicit 
first argument self, as instance methods do.

You can call a static method on the class itself, rather than on an instance 
of the class
"""
# result = MyClass.my_static_method(1, 2)
# print(result)  # Output: 3

"""
Static methods can be useful when you need to define a method that operates 
on class-level data, rather than on instance-level data. They can also be 
used to provide a utility function that is related to the class but does 
not require access to instance-level data.

Note that static methods are not the same as class methods, which also 
belong to the class rather than an instance of the class, but do receive 
an implicit first argument cls
"""




## str()
"""
In Python, the str() function is a built-in function that returns a string 
representation of an object. The object can be of any data type, and the 
string representation will depend on the type of the object.

Here are some examples of how to use the str() function:
"""
# my_int = 42
# my_str = str(my_int)
# print(my_str)  # Output: "42"
#
# my_float = 3.14159
# my_str = str(my_float)
# print(my_str)  # Output: "3.14159"
#
# my_list = [1, 2, 3]
# my_str = str(my_list)
# print(my_str)  # Output: "[1, 2, 3]"
#
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# my_str = str(my_dict)
# print(my_str)  # Output: "{'a': 1, 'b': 2, 'c': 3}"

"""
Note that the string representation of an object does not always have to 
be the same as the object's value or contents. For example, the string 
representation of a list includes the square brackets and commas that 
separate the elements, whereas the value of the list does not include 
those characters.
"""




## sum()
"""
In Python, the sum() function is a built-in function that takes an iterable 
(e.g. a list, tuple, or set) and returns the sum of all the elements in the 
iterable.

Here's an example of how to use the sum() function:
"""
# my_list = [1, 2, 3, 4, 5]
# total = sum(my_list)
# print(total)  # Output: 15

"""
The sum() function can also take an optional second argument, which specifies 
a starting value for the sum. For example:
"""
# my_list = [1, 2, 3, 4, 5]
# total = sum(my_list, 10)
# print(total)  # Output: 25




## super()
"""
In Python, the super() function is a built-in function that allows a subclass 
to call a method of its superclass. It is used to access inherited methods 
that have been overridden in a class hierarchy.

The super() function can be useful in cases where you want to override a 
method in a subclass, but still want to use the original implementation 
of the method in the superclass. By calling the superclass method using 
super(), you can avoid duplicating code and ensure that any changes made 
to the superclass method are automatically inherited by the subclass.

Here's an example of how to use the super() function:
"""
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print("The animal makes a sound.")
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#
#     def make_sound(self):
#         super().make_sound()
#         print("The dog barks.")
#
# my_dog = Dog("Fido", "Labrador")
# my_dog.make_sound()




## tuple()
"""
In Python, the tuple() function is a built-in function that creates a new 
tuple object. A tuple is an immutable sequence of elements, similar to a 
list, but with the key difference that once a tuple is created, its elements 
cannot be changed.

Tuples can be useful in situations where you want to group related data 
together, but you don't want the data to be changed accidentally. For 
example, you might use a tuple to represent a point in 2D space:

my_point = (3, 4)
In this case, my_point is a tuple containing two elements: the x-coordinate 
and y-coordinate of the point. Because tuples are immutable, you can be 
sure that the values of the x-coordinate and y-coordinate won't be changed 
accidentally.
"""
# my_list = [1, 2, 3, 4, 5]
# my_tuple = tuple(my_list)
# print(my_tuple)  # Output: (1, 2, 3, 4, 5)




## type()
"""
In Python, the type() function is a built-in function that returns the type 
of a given object. The returned type is itself an object, and can be used 
to create new instances of the same type.

Here's an example of how to use the type() function:
"""
# x = 5
# print(type(x))  # Output: <class 'int'>




## vars()
"""
In Python, the vars() function is a built-in function that returns the
__dict__ attribute of an object. This attribute is a dictionary containing 
the object's attributes and their values.

Here's an example of how to use the vars() function:
"""
# class MyClass:
#     def __init__(self):
#         self.x = 5
#         self.y = 10
#
# my_object = MyClass()
# print(vars(my_object))  # Output: {'x': 5, 'y': 10}




## zip()
"""
In Python, the zip() function is a built-in function that takes one or 
more iterable objects as input, and returns an iterator of tuples, where 
each tuple contains one element from each of the input iterables.

Here's an example of how to use the zip() function:
"""

# numbers = [1, 2, 3]
# letters = ['a', 'b', 'c']
# zipped = zip(numbers, letters)
# print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# a = [1, 2, 3]
# b = ['a', 'b']
# c = ['x', 'y', 'z']
# zipped = zip(a, b, c)
# print(list(zipped))  # Output: [(1, 'a', 'x'), (2, 'b', 'y')]




## __import__()
"""
In Python, the __import__() function is a low-level function that allows 
you to dynamically import modules at runtime. The __import__() function 
takes the name of the module as a string argument, and returns the module 
object.
"""
# my_module = __import__('math')
# print(my_module.sqrt(4))  # Output: 2.0

"""
The __import__() function can also take additional arguments to specify 
the details of the import operation, such as the package to import from, 
or the level of the import. For example:
"""
# my_module = __import__('my_package.my_module', fromlist=['my_function'], level=1)
# my_module.my_function()

"""
In this example, we use the __import__() function to import the my_function 
function from the my_module module, which is located in the my_package package. 
We also specify that we want to import at level 1, which means that we want to 
import from the parent package of the current module.

Note that while the __import__() function can be useful for dynamic importing, 
it is generally recommended to use the import statement instead for clarity 
and maintainability, unless you have a specific use case that requires the 
use of __import__()
"""
