## Module
"""
In Python, a module is a file containing Python definitions, statements,
and functions. Modules allow you to organize your Python code into reusable
pieces, and they provide a way to abstract away implementation details
and focus on higher-level concepts.

You can create your own modules by creating a Python file with a .py
extension and placing it in your project directory or any location on
your Python path. Once you have created a module, you can use it in other
Python code by importing it using the import statement.

For example, suppose you have a module called mymodule that contains a
function called my_function:

In summary, modules are an important concept in Python that allow you to
organize and reuse your code, and they form the building blocks of larger
programs and libraries.
"""


# #You can import and use this function in another Python script like this:
# import mymodule
#
# mymodule.my_function()  # prints "Hello, world!"
#
# # Alternatively, you could use the from statement to import the function directly:
# from mymodule import my_function
#
# my_function()  # prints "Hello, world!"




## package
"""
In Python, a package is a collection of modules (Python files) organized 
in a directory hierarchy. Packages are used to organize related modules 
and provide a namespace for the modules contained within them.

To create a package in Python, you simply need to create a directory with 
a special file called __init__.py inside it. This __init__.py file can be 
empty or it can contain initialization code for the package. Once you have 
created a package, you can import its modules using the import statement.

For example, suppose you have a package called mypackage that contains 
two modules module1 and module2. Here is an example of how you could import 
and use these modules:

Packages are a powerful way to organize and structure your code, especially 
for large projects with many modules. They also help to avoid naming 
conflicts between modules with the same name.
"""

# import mypackage.module1
# import mypackage.module2
#
# mypackage.module1.do_something()
# mypackage.module2.do_something_else()

# #Alternatively, you could use the from statement to import individual functions or classes from the modules:
# from mypackage.module1 import do_something
# do_something()




## Regular packages and namespace packages
"""
In Python, there are two types of packages: regular packages and namespace packages.

A regular package is a package that is organized as a directory containing 
Python modules and an __init__.py file that serves as the package initializer. 
When you import a regular package, the __init__.py file is executed, and any 
code in it is run. Regular packages can have sub-packages, which are just 
nested directories containing more Python modules and __init__.py files.

A namespace package, on the other hand, is a package that is spread across multiple 
directories or locations on the filesystem. A namespace package does not have an 
__init__.py file, but instead, it is represented by a collection of directories 
that are listed in the Python sys.path variable. When you import a namespace package, 
Python searches for all the directories that make up the package and merges them 
together into a single namespace.


Here is an example of a regular package:
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule.py

To use a regular package, you would import it like this:
import mypackage



Here is an example of a namespace package:
mypackage/
    package1/
        module1.py
    package2/
        module2.py


To use a namespace package, you would import it like this:
import mypackage.package1.module1



Note:- Namespace packages are often used in large projects that are split across 
multiple repositories or directories, or in situations where multiple packages 
need to share a common namespace.
"""