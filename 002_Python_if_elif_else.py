## if condition

"""
In Python, the if statement is used for conditional execution. It allows you to
execute a block of code only if a certain condition is true.

Here is the basic syntax for the if statement:

if condition:
    # execute this block of code if condition is true

In this syntax, condition is the expression that is evaluated to either True or False.
If the condition is True, the code inside the block following the if statement is
executed. If the condition is False, the code inside the block is skipped and the program
continues executing after the if statement.

Here's an example that demonstrates the use of an if statement:
"""

# x = 5
#
# if x > 0:
#     print("x is positive")


## else condition

"""
In Python, the else statement is used in conjunction with an if statement to 
provide an alternative block of code to execute if the condition in the if 
statement is False.

Here's the basic syntax for the if-else statement:

if condition:
    # execute this block of code if condition is true
else:
    # execute this block of code if condition is false


In this syntax, condition is the expression that is evaluated to either True or 
False. If the condition is True, the code inside the block following the if 
statement is executed. If the condition is False, the code inside the block 
following the else statement is executed.

Here's an example that demonstrates the use of the if-else statement:

"""

# x = -5
#
# if x > 0:
#     print("x is positive")
# else:
#     print("x is not positive")


## elif condition

"""
In Python, the elif (short for "else if") statement is used to add more 
conditions to the if statement. It allows you to check for multiple conditions 
and execute different blocks of code based on which condition is true.

Here's the basic syntax for the if-elif-else statement:

if condition1:
    # execute this block of code if condition1 is true
elif condition2:
    # execute this block of code if condition2 is true and condition1 is false
elif condition3:
    # execute this block of code if condition3 is true and conditions 1 and 2 are false
...
else:
    # execute this block of code if all previous conditions are false

In this syntax, you can have any number of elif statements, each with its own condition to check. 
If the first condition is true, the block of code following the if statement is executed. If the 
first condition is false and the second condition is true, the block of code following the first 
elif statement is executed, and so on. If all the conditions are false, the block of code following 
the else statement is executed.

Here's an example that demonstrates the use of the if-elif-else statement:
"""

# x = 0
#
# if x > 0:
#     print("x is positive")
# elif x < 0:
#     print("x is negative")
# else:
#     print("x is zero")