# -*- coding: utf-8 -*-
"""20221BCA0315 (02).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F8-Z1z3g3DgRi-uOMeHGl8uXgpzgtdy8

## ***Functools Module in Python***

Functools module is for higher-order functions that work on other functions.

***It provides functions for working with other functions and callable objects to use or extend them without completely rewriting them. This module has two classes – partial and partialmethod.***

***A partial function ***:

 is an original function for particular argument values.
They can be created in Python by using “partial” from the functools library. The __name__ and __doc__ attributes are to be created by the programmer as they are not created automatically.

Objects created by partial() have three read-only attributes:

Syntax:

partial(func, /, *args, **keywords)

partial.func – It returns the name of parent function along with hexadecimal address.

partial.args – It returns the positional arguments provided in partial function.

partial.keywords – It returns the keyword arguments provided in partial function.
"""

from functools import partial


def power(x, y):
	return x**y


# partial functions
pow2 = partial(power, y=2)
pow4 = partial(power, y=4)
power_of_5 = partial(power, 5)

print(power(2, 3))
print(pow2(4))
print(pow4(3))
print(power_of_5(2))

print('Function used in partial function pow2 :', pow2.func)
print('Default keywords for pow2 :', pow2.keywords)
print('Default arguments for power_of_5 :', power_of_5.args)

"""***Partialmethod class***

It is a method definition of an already defined function for specific arguments like a partial function. However, it is not callable but is only a method descriptor. It returns a new partialmethod descriptor.
"""

from functools import partialmethod

class Demo:
	def __init__(self):
		self.color = 'black'

	def _color(self, type):
		self.color = type

	set_red = partialmethod(_color, type='red')
	set_blue = partialmethod(_color, type='blue')
	set_green = partialmethod(_color, type='green')


obj = Demo()
print(obj.color)

obj.set_blue()
print(obj.color)

obj.set_red()
print(obj.color)

obj.set_green()
print(obj.color)

"""# ***Functions***

1. ***Cmp_to_key***  : It converts a comparison function into a key function.
The comparison function must return 1, -1 and 0 for different conditions.
It can be used in key functions such as sorted(), min(), max().

Syntax:

function(iterable, key=cmp_to_key(cmp_function))
"""

from functools import cmp_to_key

# function to sort according to last character
def cmp_fun(x, y):
	if x[-1] > y[-1]:
		return 1
	elif x[-1] < y[-1]:
		return -1
	else:
		return 0

list1 = ['i', 'o', 'h']
l = sorted(list1, key = cmp_to_key(cmp_fun))
print('sorted list :', l)

"""2. ## ***Reduce*** : It applies a function of two arguments repeatedly on the elements of a sequence so as to reduce the sequence to a single value.

For example, reduce(lambda x, y : x^y, [1, 2, 3, 4])

*** calculates (((1^2)^3)^4).***

If the initial is present, it is placed first in the calculation, and the default result is when the sequence is empty.

Syntax:

reduce(function, sequence[, initial]) -> value  
"""

from functools import reduce
list1 = [9,8,7,6,5,4,3,2,1]
sum_of_list1 = reduce(lambda a, b:a + b, list1)

list2 = ["abc", "xyz", "def"]
max_of_list2 = reduce(lambda a, b:a if a>b else b, list2)

print('Sum of list1 :', sum_of_list1)
print('Maximum of list2 :', max_of_list2)

"""3. ***Total_ordering :***

It is a class decorator that fills in the missing comparison methods (__lt__, __gt__, __eq__, __le__, __ge__). If a class is given which defines one or more comparison methods, “@total_ordering” automatically supplies the rest as per the given definitions. However, the class must define one of __lt__(), __le__(), __gt__(), or __ge__() and additionally, the class should supply an __eq__() method.
"""

from functools import total_ordering

@total_ordering
class N:
	def __init__(self, value):
		self.value = value
	def __eq__(self, other):
		return self.value == other.value

	# Reverse the function of
	# '<' operator and accordingly
	# other rich comparison operators
	# due to total_ordering decorator
	def __lt__(self, other):
		return self.value > other.value


print('6 > 0 :', N(6)>N(2))
print('3 < 8 :', N(3)<N(1))
print('2 <= 8 :', N(2)<= N(7))
print('9 >= 6 :', N(9)>= N(10))
print('4 == 4 :', N(5)== N(5))

"""# ***asyncio in Python***

***Asyncio is a Python library that is used for concurrent programming. It is not multi-threading or multi-processing. Asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web servers, database connection libraries, distributed task queues, etc.***

# ***Difference between Asynchronous and multi-threading programming ***

**Asynchronous programming basically means that only one part of a program will run at a certain time.**

For example, suppose we have 3 functions defined in our Python program. Consider a situation when fn1() is not doing anything, it is either asleep or just waiting or has returned a value (done its work).
So, to save the CPU time, the other function (fn2()) will start executing and then only the third function (fn3()) will execute. This is the concept of Asynchronous programming (one thing is done at one time)

***whereas, in multi-threading or multi-processing, all these three functions will run at the same time, they won’t wait for the previous function to finish or sleep***.

Note that only specific functions are made asynchronous, not the whole program this is done with the help of the Asyncio Python library.

To achieve this, an async keyword is used.

The program will wait for 1 second after it the first print statement is executed and then print the next print statement and so on.

Note that we’ll make it sleep (or wait) with the help of await asyncio.sleep(1) keyword, not with time.sleep().

 To run the program, we’ll have to use the run() function as it is given below.
"""