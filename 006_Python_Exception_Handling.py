## Exception Handling
"""
Exception handling is used in Python (and other programming languages) to handle
errors and unexpected events that can occur during the execution of a program.

When a program encounters an error, it may stop executing or produce incorrect results,
which can be a problem, especially in critical applications. Exception handling allows
developers to catch and handle these errors in a way that prevents the program from
crashing and allows it to continue executing.

In Python, exceptions are objects that represent errors or unexpected events that occur
during the execution of a program. Python provides a built-in mechanism for handling
exceptions through the "try-except" block.

The "try" block is used to execute the code that may raise an exception, and the "except"
block is used to handle the exception if it occurs. If an exception occurs in the "try"
block, the program jumps to the corresponding "except" block, and the code in that block is executed.

This allows developers to handle errors and unexpected events in a controlled way, allowing the
program to recover and continue executing. Exception handling is an essential aspect of writing robust
and reliable Python programs.
"""

## Keyword of Exception Handling:-
"""
    1. try
    2. except
    3. finally
    4. raise
    5. else
"""

## 1. try keyword
"""
In Python, the try statement is used for exception handling. It allows you to write 
code that may raise an exception and handle that exception if it occurs.

The basic syntax for using try in exception handling is as follows:

try:
    # some code that might raise an exception
except Exception:
    # code to handle the exception
"""

## 2. except keyword
"""
In Python, the except keyword is used for handling exceptions in a try statement. The except 
block catches and handles exceptions that are raised in the corresponding try block.

The basic syntax for using except in exception handling is as follows:

try:
    # some code that might raise an exception
except Exception:
    # code to handle the exception
    
In this example, the try block contains code that might raise an exception. 
If an exception is raised, the control is transferred to the except block, which contains 
code to handle the exception. The Exception after the except keyword specifies the type of 
exception to be handled. You can specify different types of exceptions by using multiple except blocks.

Here's an example of using multiple except blocks:

try:
    # some code that might raise an exception
except ValueError:
    # code to handle the ValueError exception
except TypeError:
    # code to handle the TypeError exception

In this example, the try block contains code that might raise a 
ValueError or TypeError exception. If a ValueError exception is 
raised, the control is transferred to the first except block, which 
contains code to handle the ValueError exception. If a TypeError 
exception is raised, the control is transferred to the second except 
block, which contains code to handle the TypeError exception.
"""

# while (True):
#     try:
#         a = int(input("Enter an number "))
#         b = int(input("Enter an number "))
#         c = a / b
#         print(c)
#         break
#
#     except ZeroDivisionError as e:
#         print(e)
#
#     except ValueError as e:
#         print(e)

## 3. finally keyword
"""
In Python, the finally keyword is used in the context of exception handling. 
It is used to define a block of code that will be executed no matter what happens 
in the try and except blocks.

try:
    # code that might raise an exception
except:
    # code to handle the exception
finally:
    # code to be executed regardless of whether an exception was raised or not

The try block contains the code that might raise an exception. If an exception is raised, 
the control is transferred to the except block. The except block contains code to handle the 
exception. The finally block contains code that will be executed regardless of whether an 
exception was raised or not.

The finally block is often used for tasks such as releasing resources (e.g., closing files or 
network connections) or cleaning up after an operation (e.g., resetting variables). The code in 
the finally block is guaranteed to execute, even if an unhandled exception is raised.
"""

# try:
#         a = int(input("Enter an number "))
#         b = int(input("Enter an number "))
#         c = a/b
#         print(c)
#
# except (ZeroDivisionError, ValueError) as e:
#     print(e)
#
# finally:
#     print("It will execute always whether an exception was raised or not")

## 4. raise keyworkd
"""
In Python, the raise keyword is used to manually raise an exception. It is typically used in 
exception handling to signal that an error or exceptional condition has occurred.

The basic syntax for using raise to raise an exception is as follows:

    raise Exception("Error message")

In this example, Exception is the type of exception being raised, and "Error message" is the error 
message associated with the exception. The error message can be any string that describes the reason 
for the exception.

You can also raise an exception without specifying an error message:

    raise Exception

In this case, a generic Exception is raised without an error message.

You can use the raise keyword in conjunction with the try and except blocks to handle exceptions in your code. 

For example:

try:
    # some code that might raise an exception
except Exception:
    # code to handle the exception
raise

In this example, the try block contains code that might raise an exception. If an exception is raised, 
the control is transferred to the except block, which contains code to handle the exception. The raise 
statement in the except block re-raises the exception, so it can be handled by higher-level exception 
handlers or by Python's default exception handling mechanism.

You can also create your own custom exceptions by subclassing the built-in Exception class or one of its subclasses. 
For example:

class MyException(Exception):
    pass
    
raise MyException("Custom error message")

In this example, a custom exception called MyException is defined by subclassing the built-in Exception class. 
The raise statement is then used to raise an instance of MyException with a custom error message.

Overall, the raise keyword is an important part of exception handling in Python, allowing you to signal that an 
error or exceptional condition has occurred in your code.
"""

# try:
#     a = int(input("Input first no: "))
#     b = int(input("Input second no: "))
#     if a < 0 or b < 0:
#         raise Exception("a and b should be greater than 0")  # Custom error message
#     c = a / b
#     print(" Div is ", c)
# except Exception as e:
#     print(e)

## 5. else keyword
"""
In Python, the else keyword is used in the context of exception handling to specify a block of code to be executed 
if no exception is raised in the try block.

The basic syntax for using else in exception handling is as follows:

try:
    # some code that might raise an exception
except Exception:
    # code to handle the exception
else:
    # code to be executed if no exception is raised

In this example, the try block contains code that might raise an exception. If an exception is raised, the control is 
transferred to the except block, which contains code to handle the exception. If no exception is raised, the control 
is transferred to the else block, which contains code to be executed if no exception is raised.

The else block is optional and can be omitted if there is no code to be executed if no exception is raised. The else 
block is often used to perform cleanup tasks or to execute code that is dependent on the successful completion of the try block.

Here's an example of using else in exception handling:

try:
    # some code that might raise an exception
except ValueError:
    # code to handle the ValueError exception
except TypeError:
    # code to handle the TypeError exception
else:
    # code to be executed if no exception is raised
finally:
# code to be executed regardless of whether an exception was raised or not

In this example, the try block contains code that might raise a ValueError or TypeError exception. If a ValueError exception is raised, 
the control is transferred to the first except block, which contains code to handle the ValueError exception. If a TypeError exception is 
raised, the control is transferred to the second except block, which contains code to handle the TypeError exception. If no exception is 
raised, the control is transferred to the else block, which contains code to be executed if no exception is raised. Finally, the finally 
block contains code that will be executed regardless of whether an exception was raised or not.
"""


# try:
#     a = int(input("Input first no: "))
#     b = int(input("Input second no: "))
#     c = a/b
#     print("Div is ", c)
#     print("\n")
# except (ZeroDivisionError, ValueError) as e:
#     print("Error name:- ",e)
# else:
#     print("Code successfully executed.")


"""
Use of sys.exc_info¶
In Python, sys.exc_info() is a function that returns information about the last exception that was raised in the program.

The function returns a tuple containing three items:

The type of the exception (as a Python class):
The exception object itself (an instance of the exception class)
A traceback object (which contains information about the location in the program where the exception was raised) You 
can use sys.exc_info() in a try-except block to catch an exception and handle it appropriately. For example:

import sys
try:
    # code that may raise an exception
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()

# handle the exception
In this example, if an exception is raised within the try block, sys.exc_info() is called to get information about the 
exception. The exc_type variable contains the type of the exception (such as ValueError, TypeError, etc.), exc_value 
contains the exception object (which can be used to access information about the exception), and exc_traceback contains 
the traceback object (which can be used to print out the stack trace).

Note that sys.exc_info() should only be called within an exception handler (except block), and should not be called in 
normal code flow. Additionally, it's important to call sys.exc_info() as soon as possible after the exception is raised, 
since the information it provides may be overwritten by subsequent exceptions.
"""


# import sys
#
# try:
#     a = int(input("Input first no: "))
#     b = int(input("Input second no: "))
#     c = a/b
#     print(" Div is ", c)
# except:
#     a,b,c = sys.exc_info()
#     print("Exception type: - ", a)
#     print("Exception value: - ", b)
#     print("Exception traceback: - ", c)
#     print("Line number: - ", c.tb_lineno) # print line number in which exception will occur



"""
Discussion:-
1. What is exception
2. How to handle exception
3. use of try, except, else, raise, finally
4. use of sys.exc_inof()(for getting entire detail of the exception)
5. rasise keyword(At any line if we want to raise the exception we can use raise)
"""