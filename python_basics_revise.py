# -*- coding: utf-8 -*-
"""Python_Basics_revise.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lhyfEEtPRbvytsgnKalwAFpVdUmvP5RQ
"""

name = input("Enter your name: ")
print("Hello, ", name)
#output statement with keyword arguments
print("Hello", "World", sep=", ", end="!\n")
# The end keyword argument to specify what character(s) should be printed at the end of the output (instead of the default newline \n).
# The sep keyword argument allows you to specify the separator string that will be used between the arguments passed to print()

#date types in python
int_from_float = int(3.14)
float_from_int = float(10)
string_from_int = str(100)
list_from_string = list("Hello")
tuple_from_list = tuple([1, 2, 3, 4, 5])
set_from_list = set([1, 2, 3, 4, 5])

print(int_from_float)
print(float_from_int)
print(string_from_int)
print(list_from_string)
print(tuple_from_list)
print(set_from_list)
#just convert data types in to each other

#conditional Statement
a = 10
b = 5

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")

#jumping statement
#break statement -------------The break statement terminates the current loop and transfers control to the next statement outside the loop.
for i in range(1, 19):
  if i == 10:
    break
    print(i)

#continue statement --------------The continue statement skips the current iteration of the loop and moves to the next iteration. Both break and continue can be used in both for and while loops.
for i in range(1, 24):
  if i == 20:
    continue
    print(i)

# Special Functions
fruits = ["apple", "banana", "cherry"]

# len()
print(len(fruits))  # Output: 3

# id()
print(id(fruits))  # Output: Unique ID of the list object    The id() function returns the unique identifier (memory address) of an object.

# type()
print(type(fruits))  # Output: <class 'list'>

# range()
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

#sets
my_set = {1,2,3,4,5,6}
another_set = set([4,5,6,7,8]) #thats how we convert a list to set
print("Set created using '{}' curly brackets: ", my_set)
print("Set created using constructor: ", another_set)

grocery_list = {"apples", "bananas", "milk", "bread"}
household_list = {"detergent", "paper towels", "milk", "bread"}

#union(|)
shopping_list = grocery_list | household_list
print("Shopping list: ",shopping_list)

#interaction(&)
shopping1_list = grocery_list & household_list
print("Shopping list: ", shopping1_list)


#difference(-)
set1 = {1,2,3}
set2 = {3,4,5}
difference_set = set1 - set2
print("Difference set: ", difference_set)


#symmetric Difference(^). it shows us only unique sets form different set
symmetric_difference_set = set1 ^ set2
print("Symmetric difference set: ", symmetric_difference_set)

squa = {x * x for x in range(1, 6)}
print(squa)

#cartesian product:
set1 = {1, 2, 3}
set2 = {'a', 'b', 'c'}

cartesian_product = {(x, y) for x in set1 for y in set2}
print(cartesian_product)

#to use power set
def power_set(a):
  if len(a) == 0:
    return {frozenset()}
  element = a.pop()
  subsets = power_set(a)
  return subsets.union({subset.union({element}) for subset in subsets})
my_set = {1,2,3}
print(power_set(my_set))

#A frozenset is an immutable version of a set, meaning its elements cannot be changed after creation. This operation is useful when you need to create a set that remains constant and cannot be modified.
my_set = {1, 2, 3}
frozen_set = frozenset(my_set)
print(frozen_set)

#functions
def nish(name):  #fucntion definition with parameter 'name'
  """this function for verification in code."""
  print("Hello, " + name + "!")

nish("Nishant") #function call

def calculate_area(lenght, width):
  return lenght * width

area = calculate_area(3, 9)
print(area)

def greet(name, mass = "jelly"):
  print(mass, name + " @!")
greet(mass = "hi", name= "nish")
greet("rahul")   #jelly use for default system

def cal_ave(*numbers):
  if len(numbers) == 0:
    return 0
  total = sum(numbers)
  return total / len(numbers)

average = cal_ave(1, 2, 3, 4, 5)
print(average)

cal_ave()

#lambda fucntions  ----------given two numbers and then uses of these two numbers
add = lambda x, y: x + y
result = add(3, 5)
print(result)

greeting = lambda name: f"Hello, {name}!"
print(greeting("nsih"))

words = ["apple", "banana", "dates", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#map reduce functions
#The map function applies a given function to all elements of an iterable (like a list) and returns an iterator containing the transformed elements.
numbers = [1,2,3,4,5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

numbers = [1, 2, 3, 4, 5, 6]

# Filtering even numbers using filter() and a lambda function
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# filter() also returns an iterator, convert it to a list for printing
print(list(even_numbers))  # Output: [2, 4, 6]

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce() to find the product of all elements in the list
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 120

x = 10
def my_fuc():
  y = 20
  print("Inside function: ", x,y)
  def inner_fuc():
    z = 30
    print("Inside inner function: ", x,y,z)
  inner_fuc()
print("Outsider fucntion: ", x)
my_fuc()

#Area calculator. for rectangle---------
def calculate(lenght, width):
  area = lenght * width
  return area
calculate(4,6)

#String Manipulation
def reverse_string(input_string):
  return input_string[::-1]
reverse_string("nishant")

#list Statistics
def analyze_list(numbers):
  if not numbers:
    return None
  average = sum(numbers) / len(numbers)
  maximum = max(numbers)
  minimum = min(numbers)
  return average, maximum, minimum
analyze_list([1,2,3,4,5])

#filtering and lambda
def filter_short_names(names, max_length):
  return list(filter(lambda name: len(name) <= max_length, names))
filter_short_names("nishant", 10)

#text Analyzer
def analyze_text(text):
  words = text.split()
  word_count = len(words)
  char_count = len(text)
  return word_count, char_count
analyze_text("hello world")