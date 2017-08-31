'''
if statements in python allows us to tell the computer to perform
alternative actions based on a certain set of results
'''
loc = 'Auto Body'

if loc == 'Auto Shop':
    print('welcome to the Auto Shop')
elif loc = 'Bank':
    print("let's go to bank")
else:
    print('where are you')


'''
A for loop acts as an iterator in python, it goes throught items
that are in a sequence or any other iterable item
'''

l = [1,2,3,4,5]

for num in l:
    print(num)

s = 'abcdefg'

for string in s:
    print(string)

tup = (1,2,3,4,5)

for t in tup:
    print(t)


dic = {'k1':1,'k2':2, 'k3':3}

for key in d:
    print(key)

for (k,v) in d.items():
    print(k)
    print(v)


x = 0
while x < 10:
    print('x is currently : ', x)
    x += 1

'''
while test:
    code statement
    if test:
        break
    if test:
        continue
else:
'''

range(10)
x = range(0,10)#[0,1,2,3,4,5,6,7,8,9]
type(x)#list

x = xrange(1,6)
type(x)#xrange

'''
range() outputs a list, xrange() will generate elements but not save them 
in memory
'''


#comprehensions

l = []

for letter in 'word':
    l.append(letter)

lst = [letter for letter in 'word']
lst = [x ** 2 for x in xrange(0,11)]
lst = [number for number in range(11) if number % 2 == 0]



