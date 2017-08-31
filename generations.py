'''generators
generator functions allow us to write a function
that can send back a value and then later resume
to pick up where it left off. 

The main difference in syntax will be the use of a yield statement
'''

def gencubes(n):
    for num in range(n):
        yield num**3

def genfibon(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a = b
        b = a + b