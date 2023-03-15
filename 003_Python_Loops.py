## for loop

"""
In Python, a for loop is used to iterate over a sequence (such as a list,
tuple, or string) or other iterable object. It allows you to execute a
block of code repeatedly for each item in the sequence.

Here's the basic syntax for the for loop:

for item in sequence:
    # execute this block of code for each item in the sequence

In this syntax, item is a variable that takes on the value of each item in
the sequence one at a time, and sequence is the iterable object that contains
the items to be iterated over. The code inside the block following the for
statement is executed once for each item in the sequence, with item taking on
the value of each item in turn.

Here's an example that demonstrates the use of the for loop:
"""

# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     print(fruit)


## range function
"""
Note that the range() function is often used with the for loop to iterate over a 
range of numbers. Here's an example:
"""

# for i in range(1, 6):
#     print(i)


## while loop

"""
In Python, a while loop is used to repeatedly execute a block of code as long as 
a certain condition is true. It is often used when you don't know the number of 
times you need to execute a loop beforehand.

Here's the basic syntax for the while loop:

while condition:
    # execute this block of code as long as condition is true
    
In this syntax, condition is an expression that is evaluated to either True or 
False. The code inside the block following the while statement is executed 
repeatedly as long as the condition is true.

Here's an example that demonstrates the use of the while loop
"""

# i = 1
#
# while i <= 5:
#     print(i)
#     i += 1


"""
Note that it's important to make sure that the condition in the while loop 
eventually becomes False, otherwise the loop will execute indefinitely and 
your program will become stuck in an infinite loop.
"""


## break statement
"""
In Python, the break statement is used to exit a loop prematurely. When a 
break statement is encountered inside a loop, the loop is immediately 
terminated and program execution resumes at the statement immediately following 
the loop.

Here's an example that demonstrates the use of the break statement in a while loop:

"""
# i = 1
#
# while i <= 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
#
# print("Loop finished")


"""
Note that the break statement can be used inside a for loop, while loop, or 
nested loops. It's often used in conjunction with an if statement to 
conditionally exit a loop based on a certain condition.
"""


## continue statement
"""
In Python, the continue statement is used inside a loop to skip the current 
iteration of the loop and move on to the next iteration. When a continue 
statement is encountered inside a loop, the loop immediately skips to the 
next iteration and continues executing the loop from there.

Here's an example that demonstrates the use of the continue statement in a for loop:
"""

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)
#
# print("Loop finished")

"""
Note that the continue statement can be used inside a for loop or while loop. 
It's often used in conjunction with an if statement to conditionally skip 
certain iterations of a loop based on a certain condition.
"""