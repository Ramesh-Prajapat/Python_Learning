# **Class**

"""
In Python, everything is an object. A class is a blueprint for the object. To create an object we require a model or plan or blueprint which is nothing but class.

We create class to create an object. A class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object. The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.

Class represents the properties (attribute) and action (behavior) of the object. Properties represent variables, and actions are represented by the methods. Hence class contains both variables and methods.

We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. Here, a parrot is an object.
"""

# **Object**
"""

The physical existence of a class is nothing but an object. In other words, the object is an entity that has a state and behavior.

Therefore, an object (instance) is an instantiation of a class. So, when class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

Syntax:

reference_variable = classname()
"""

# **Instance Variables and Methods**
"""

If the value of a variable varies from object to object, then such variables are called instance variables. For every object, a separate copy of the instance variable will be created.

When we create classes in Python, instance methods are used regularly. we need to create an object to execute the block of code or action defined in the instance method.

We can access the instance variable and methods using the object. Use dot (.) operator to access instance variables and methods.

In Python, working with an instance variable and method, we use the self keyword. When we use the self keyword as a parameter to a method or with a variable name is called the instance itself.

Note: Instance variables are used within the instance method
"""


# class Student:
#     def __init__(self, name, percentage):
#         self.name = name  # Instance variable
#         self.percentage = percentage  # Instance variable
#
#     def show(self):  # Instance Method
#         print("Name is:", self.name, "and percentage is:", self.percentage)
#
#
# stud = Student("Arthur", 90)
# stud.show()
#
# # Output Name is: Arthur and percentage is: 90



# class Parrot:
#     species = "bird"                    # class attribute
#     def __init__(self, name, age):      # instance attribute
#         self.name = name
#         self.age = age
#
# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)
#
# # access the class attributes
# print("Blu is a {}".format(blu.__class__.species))
# print("Woo is also a {}".format(woo.__class__.species))
#
# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))

# **Object Method**
"""

Object Methods are functions defined inside the body of a class. They are used to define the behaviors of an object.

Objects can have methods. The methods are functions which belong to the object.
"""

# **Object Default Methods**
"""

Sometimes, you may want to have a default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters. Let's see how it looks:
"""


# **What is self in Python?**
"""
In object-oriented programming, whenever we define methods for a class, we use self"""


# **Constructors in Python**
"""

In Python, if a class functions that begin with double underscore __ are called special functions as they have special meaning.

A class without a constructor is not really useful in real applications. A constructor is a special type of method used in Python to initialize the object of a Class. The constructor will be executed automatically when the object is created. If we create three objects, the constructor is called three times and initialize each object.

The main purpose of the constructor is to declare and initialize instance variables. It can take at least one argument that is self. The init() method is called the constructor in Python. In other words, the name of the constructor should be init(self).

A constructor is optional, and if we do not provide any constructor, then Python provides the default constructor. Every class in Python has a constructor, but it’s not required to define it.
"""

# **Types of Constructors**
"""

We have two types of constructors in Python:

Non-parameterized:The constructors in Python which have no parameter is known as a non parameterized constructor. The non-parameterized constructor uses when we do not want to manipulate the value or the constructor that has only self as an argument.

Parameterized Constructor: The constructor with parameters is known as a parameterized constructor. The parameterized constructor has multiple parameters along with the self.
"""

## 1. Non-parameterized constructor
# class Animal:
#     def __init__(self):
#         print("This is non parameterized constructor.")
#
# obj = Animal()


## 2. Parameterized constructor

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f"Animal name is {self.name}")
#         print(f"Animal age is {self.age}")
#
#
# obj = Animal("dog", 12)
# obj.show()


# **Python Inheritance**
"""

The process of inherting the properties of the base (or parent) class into a derived (or child) class is called inheritance. Inheritance enables us to define a class that takes all the functionality from a base class and allows us to add more.
"""

# **Inhritance in Python**
"""

the main purpose of inheritance is the reusability of code because we can use the existing class to a new class insted of creating it from scratch.

Syntax:

class BaseClass:
    Body of base class
class DerviedClass(BaseClass):
    Body of derived class
"""

# **Type of Inheritance**

"""

In Python, based upon the number of child and parent classes involved, there are five types of inheritance. The type of inheritance are listed below:

Single Inheritance
Multiple Inheritance
Multilevel Inheritance
Hierarchical Inheritance
Hybrid Inheritance
"""
# **Python Single Inheritance**
"""

In single inheritance, a derived class inherits from a single-base class. Here in one derived class and one base class.
"""


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def show(self):
#         print(f"This is a {self.name}")
#         print(f"And it's age is {self.age}")
#
#
# obj1 = Dog("Dog", 12)
# obj1.show()

# **Python Multiple Inheritance**
"""

In multiple inheritance, one derived class can inherit from multiple base classes.
"""


# class A:
#     def __init__(self):
#         print("This is class A")
#         super().__init__()
#
#
# class B:
#     def __init__(self):
#         print("This is class B")
#         # super().__init__()
#
#
# class C(A, B):
#     def __init__(self):
#         print("This is class C")
#         super().__init__()
#
#
# obj = C()


# **Python Multilevel Inheritance**
"""

In multilevel inheritance, we can also inherit from a derived class. It can be of any depth in Python.

All the features of the base class and the derived class are inherited into the new derived class.

For example, there are three classes A, B, C. A is the superclass, B is the child class of A, C is the child class of B. In other words, we can say a chain of classes is called multilevel inheritance.
"""


# class A:
#     def __init__(self):
#         print("This is class A")
#         # super().__init__()
#
#
# class B(A):
#     def __init__(self):
#         print("This is class B")
#         # super().__init__()
#
#
# class C(B):
#     def __init__(self):
#         print("This is class C")
#         super().__init__()
#
#
# obj = C()


# **Python Hierarchical Inheritance**
"""

In Hierarchical inheritance, more than one child class is derived from a single parent class. In other words, we can say one base class and multiple derived classes.
"""


# class Vehicle:
#     def __init__(self):
#         print("This is Vehicle")
#
#
# class Car(Vehicle):
#     def carInfo(self, name):
#         print("Car name is: ", name)
#
#
# class Truck(Vehicle):
#     def truckInfo(self, name):
#         print("Truck name is: ", name)
#
#
# obj1 = Car()
# obj1.carInfo("BMW")
#
# print("\n")
# obj2 = Truck()
# obj2.truckInfo("Ford")

# Python Hybrid Inheritance
"""

When inheritance is consists of multiple types or a combination of different inheritance is called hybrid inheritance.
"""


# **The Super Method**
"""

The super() built-in function returns a proxy object, a substitute object that can call methods of the base class via delegation. This is called indirection (ability to reference base object with super() built-in function)

# **Why super() keyword

The super() function is most commonly used with init function in base class. This is usually the only place where we need to do some things in a child then complete the initialization in the parent.

class Child(Parent):

def __init__(self, stuff)
    self.stuff = stuff
    super().__init__()
Benefits of using the super() function are:

We are not required to remember or specify the parent class name to access its methods.
We can use the super() function in both single and multiple inheritances.
The super() function support code reusability as there is no need to write the entire function
"""


# class A:
#     def __init__(self, name):
#         self.name = name
#
#
# class B(A):
#     def __init__(self, name, age):
#         self.age = age
#         super().__init__(name)
#
#     def show(self):
#         print(f"Hello I'm {self.name}")
#         print(f"And I'm {self.age} old")
#
#
# obj = B("Ramesh", 22)
# obj.show()

# **Method Resolution Order in Python**
"""

In Python, Method Resolution Order(MRO) is the order by which Python looks for a method or attribute. First, the method or attribute is searched within a class, and then it follows the order we specified while inheriting.

This order is also called the Linearization of a class, and a set of rules is called MRO (Method Resolution Order). The MRO plays an essential role in multiple inheritances as a single method may found in multiple parent classes.

In multiple inheritance, the following search order is followed.

First, it searches in the current parent class if not available, then searches in the parents class specified while inheriting (that is left to right.) We can get the MRO of a class. For this purpose, we can use either the mro attribute or the mro() method.
"""


# class A:
#     def __init__(self):
#         print("Parent class.")
#
#
# class B:
#     def __init__(self, first_name):
#         self.first_name = first_name
#
#
# class C(B, A):
#     def __init__(self, first_name, last_name):
#         self.last_name = last_name
#         super().__init__(first_name)  # Access method and attribute of B class using Super method
#         A.__init__(self)  # Call to parent class method
#
#     def info(self):
#         print(f"First name is {self.first_name}.")
#         print(f"Last name is {self.last_name}.")
#
#
# obj = C("Ramesh", "Chand")
# obj.info()



# **Encapsulation**
"""

In Python, encapsulation is a method of wrapping data and functions into a single entity. For example, A class encapsulates all the data (methods and variables). Encapsulation means the internal representation of an object is generally hidden from outside of the object’s definition.

Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single _ or double __.
"""


# class Computer:
#
#     def __init__(self):
#         self.__maxprice = 900  # Private variable
#         self._name = "HP"  # Protected variable
#
#     def sell(self):
#         print("Selling Price: {}".format(self.__maxprice))
#
#     def setMaxPrice(self, price):
#         self.__maxprice = price
#
#
# class OtherComputer(Computer):
#     def __init__(self):
#         super().__init__()
#
#     def show(self):
#         print("Computer name is ", self._name)
#         print("Max price of other computer is", self.__maxprice)
#
#
# # Created object of partent class
# c = Computer()
# c.sell()
#
# # Created object of child class
# oc = OtherComputer()
# oc.show()


# **Polymorphism**
"""

Polymorphism is based on the greek words Poly (many) and morphism (forms). We will create a structure that can take or use many forms of objects.

Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

Example 1: The student can act as a student in college, act as a player on the ground, and as a daughter/brother in the home.

Example 2: In the programming language, the + operator, acts as a concatenation and arithmetic addition.

Example 3: If we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape.
"""


# class Parrot:
#     def fly(self):
#         print("Parrot can fly")
#
#     def swim(self):
#         print("Parrot can't swim")
#
#
# class Penguin:
#     def fly(self):
#         print("Penguin can't fly")
#
#     def swim(self):
#         print("Penguin can swim")
#
#
# # common interface
# def flying_test(bird):
#     bird.fly()
#
#
# # instantiate objects
# blu = Parrot()
# peggy = Penguin()
#
# # passing the object
# flying_test(blu)
# flying_test(peggy)


# class Circle:
#     pi = 3.14
#
#     def __init__(self, redius):
#         self.radius = redius
#
#     def calculate_area(self):
#         print("Area of circle:", self.pi * self.radius * self.radius)




# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculate_area(self):
#         print("Area of Rectangle:", self.length * self.width)
#
# cir = Circle(9)
# rect = Rectangle(9, 6)
# cir.calculate_area()   # Output Area of circle: 254.34
#
# rect.calculate_area()  # Output Area od Rectangle: 54


# **Method Overriding**
"""

In inheritance, all members available in the parent class are by default available in the child class. If the child class does not satisfy with parent class implementation, then the child class is allowed to redefine that method by extending additional functions in the child class. This concept is called method overriding.

When a child class method has the same name, same parameters, and same return type as a method in its superclass, then the method in the child is said to override the method in the parent class.
"""


# class Vehicle:
#     def max_speed(self):
#         print("max speed is 100 Km/Hour")
#
# class Car(Vehicle):
#     # overridden the implementation of Vehicle class
#     def max_speed(self):
#         print("max speed is 200 Km/Hour")
#
# # Creating object of Car class
# car = Car()
# car.max_speed()



# class Bird:
#
#     def __init__(self):
#         print("Bird is ready")
#
#     def whoisThis(self):
#         print("Bird")
#
#     def swim(self):
#         print("Swim faster")




# child class
# class Penguin(Bird):
#
#     def __init__(self):
#         # call super() function to run the __init__() method of the parent class inside the child class.
#         super().__init__()
#         print("Penguin is ready")
#
#     def whoisThis(self):
#         print("Penguin")
#
#     def run(self):
#         print("Run faster")
#
#
# peggy = Penguin()
# peggy.whoisThis()
# peggy.swim()
# peggy.run()
#
# # issubclass(Penguin, Bird)
# isinstance(peggy, Bird)