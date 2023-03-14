##1-3. Python Numbers
"""

Integers, floating point numbers and complex numbers fall under Python numbers category. They are defined as int, float and complex classes in Python.

We can use the type() function to know which class a variable or a value belongs to.

Similarly, the isinstance() function is used to check if an object belongs to a particular class. Integers can be of any length, it is only limited by the memory available.

A floating-point number is accurate up to 15 decimal places. Integer and floating points are separated by decimal points. 1 is an integer, 1.0 is a floating-point number.

Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part. Here are some examples.
"""


## int
# a = 5
# print(type(a))
# print(5)


## isinstance
#print(isinstance(5, int))

## float
# a = 5.01
# print(type(a))
# print(a)


## complex
# a = 1+2j
# print(type(a))
# print(a)




##4. Python Boolean - True, False


##5. Python Strings
"""

String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, ''' or "".

Just like a list and tuple, the slicing operator [ ] can be used with strings. Strings, however, are immutable.
"""

#
# name = 'Ramesh Chand Prajapat'
# print(type(name))
# print(name)

# name = 'Ramesh Banwal'
# name[7:13]


##6. Python List
"""
List is an ordered sequence of items. It is one of the most used datatype in Python and is very flexible. All the items in a list do not need to be of the same type.

Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets []

Lists are mutable, meaning, the value of elements of a list can be altered.

Here are some list function(external)-

1. append
2. pop 
3. insert
4. remove
5. extend
6. index
7. count
8. sort
9. clear
"""


## append

# num = [11, 22, 33, 44, 55]
# num.append(100)
# print(num)


## pop

# num = [11, 22, 33, 44, 55]
# num.pop(2)
# num.pop()
# print(num)



## insert

# num = [11, 22, 33, 44, 55]
# num.insert(2, 100)
# print(num)



## extend

# num1 = [11, 22, 33, 44]
# num2 = [55, 66, 77, 88]
# num1.extend(num2)
# print(num1)


## index
#
# num = [11, 22, 33, 44, 55]
# print(num.index(22))
# print(num.index(44, 2, 4))


## count

# num = [11, 22, 33, 44, 11, 11]
# print(num.count(11))



## sort

# num = [11, 55, 22, 66, 33]
# num.sort()
# print(num)
#
# num1 = [11, 55, 22, 66, 33]
# num1.sort(reverse=True)
# print(num1)


## clear

# num = [11, 22, 33, 44, 55]
# num.clear()
# print(num)

##7. Python Tuple
"""
Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.

It is defined within parentheses () where items are separated by commas.

We can use the slicing operator [] to extract items but we cannot change its value.

Here are some tuple method(external):-

1. index
2. count

NOTE:-  If you want to apply more method on tuple so you can,
        but before it you must change/convert tuple to list."""

## index

# num = (11, 22, 33, 44)
# print(num.index(22))


## count

# num = (11, 22, 33, 22, 44, 55, 22)
# print(num.count(22))

##8. Set
"""
Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.

We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates. Since, set are unordered collection, indexing has no meaning. Hence, the slicing operator [] does not work.

Here are some method(external):-

1. add
2. remove
3. union
4. intersection
5. difference_update"""

## add

# num = {11, 22, 33, 44, 55}
# num.add(66)
# print(num)


## remove

# num = {11, 22, 33, 44, 55}
# num.remove(22)
# print(num)


## union

# num1 = {11, 22, 33, 44, 55}
# num2 = {11, 33, 66, 77}
# print(num1.union(num2))



## intersection

# num1 = {11, 22, 33, 44, 55}
# num2 = {33, 44, 66, 77}
# print(num1.intersection(num2))



## difference_update

# num1 = {'ramesh', 'rajat', 'kuldeep'}
# num2 = {'ramesh', 'pradeep', 'harshit'}
# print(num1.difference_update(num2))


##9. Python Dictionary
"""
Dictionary is an unordered collection of key-value pairs.

It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.

In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.

We use key to retrieve the respective value. But not the other way around.

Here are some method(external) of dictionary:-

        1. get
        2. items
        3. keys
        4. values"""


## get
#
# person = {'ramesh':23, 'kuldeep': 24, 'rajat': 21, 'deepak': 22}
# print(person.get('ramesh'))


## itmes

# person = {'ramesh':23, 'kuldeep': 24, 'rajat': 21, 'deepak': 22}
# print(person.items())


## keys

# person = {'ramesh':23, 'kuldeep': 24, 'rajat': 21, 'deepak': 22}
# print(person.keys())


## values

# person = {'ramesh':23, 'kuldeep': 24, 'rajat': 21, 'deepak': 22}
# print(person.values())