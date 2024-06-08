#Inheritance provides code 

class Square:
  def what_shape(self):
    print("that's gonna take a copy from their.")

class Square(Square):  
  pass  
square = Square()

square.what_shape() 


# parent class is animal by this we can see that which animal make what sound according to that we make a child class like dog make woof sound we and cat make meow so we inherit parent class in it.
'''
class Animal:
  def make_sound(self):
    print("animal sound")

class Dog(Animal):
  def make_sound(self):
    print("Woo!")

class Cat(Animal):
  def make_sound(self):
    print("Meow!")

class Poodle(Dog):  # Poodle inherits from Dog
  pass

animals = [Animal(), Dog(), Cat(), Poodle()]
for animal in animals:
  animal.make_sound()

  '''

#Single inheritance:
'''
class Parent: 
  
  def speak(self):
    print("Making animal sounds")

class Dog(Animal):
my_dog = Dog()
my_dog.speak()
'''


#Multiple inheritance:  
'''class School: 
  def identify(self):
    print("I am a School.")

class Students: 
  def identify(self):
    print("I am an Students.")

class Education(School, Students):  #Child class
  pass
my = Education()
my.identify()
'''

#Multilevel Inheritance:
'''
class Shape:  
  def area(self):
    raise NotImplementedError

class Square(Shape):  
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side * self.side

class ColoredSquare(Square):  
  def __init__(self, side, color):
    super().__init__(side)
    self.color = color

  def describe(self):
    return f"A {self.color} square and area {self.area()}"
my_square = ColoredSquare(40, "Red")
print(my_square.describe())  
'''



#Hierarchial: 
'''
class Parental:
	def func1(self):
		print("parent class.")
class Child1(Parent)
	def func2(self):
		print("This child 1.")
class Child2(Parent)
	def func3(self):
		print("This child 2.")
object1 = Child1()
object2 = Child2()
object1.func2()
object2.func3()
'''

#TRY AND EXCEPT: 
'''
x = 19
y = 0
try:
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Error: shouldn't be divided by it")

'''
#Finally block
'''def divide(num1, num2):
  try:
    result = num1 / num2
  except ZeroDivisionError:
    print("Error")
  finally:
    print("Division attempted.")
divide(10, 5)  
divide(19, 0)
'''


#BUILT-IN EXCEPTION
'''
try:
    if x == 9:
        print("x is equal to 5")
except SyntaxError:
    print("SyntaxError occurred")
'''


#Indentation error

'''try:
    def my_func():
        print("Inside function")
except IndentationError:
    print("IndentationError occurred")


'''


#TypeError
'''
try:
    x = "hello, there could be an error may be"
    y = 190
    print(x + y) 
except TypeError:
    print("TypeError occurred")

'''



#VALUE ERROR
'''
try:
    
    int("Heh, it's minions operation for begin a banana party")  
except ValueError:
    print("ValueError occurred")
'''