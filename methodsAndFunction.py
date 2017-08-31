''' 
methods are essentially functions built into objects
'''

l = [1,2,3,4,5]

'''
functions is a useful device that groups together a 
set of statements so they can be run more than once.
They can also let us specify parameters that can serve as
inputs to the functions
'''

def name_of_function():
    pass#it is not going to do anything


'''lambda expression
one of pythons most useful tools, it allows us to create
anonymous functions. That means we can quickly make a function
without needing to properly define a function using def
'''

def square(num):
    result = nums**2
    return result

square(2)

#one line function
square = lambda nums:nums**2

first = lambda s: s[::-1]

adder = lambda x,y: x + y


'''nested statements and scopes
when we crate a variable name in python, the name is 
stored in a namespace, variable names also have a scope,
the scope determines the visibility of that variable name
to other parts of your code. 
Name assignments will crate or change local name by default
4 scopes in python:
local: names assigned within a fucntion
enclosing functions: in enclosing function
global: at top level of the code
built-in
'''


##global statement
x = 1
def func():
    global x
    x = 2
    pass


