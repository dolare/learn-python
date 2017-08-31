'''map
is a function that takes two arguments: a function and a sequence
iterable. map(function,sequence)
'''

def fahrenheit(T):
     return 9/5 * T + 32

temp = [0,1,5,7]

map(fahrenheit,temp)

map(lambda T : 9/5 * T + 32,temp)


'''reduce
'''

lst = [47,11,42,13]
reduce(lambda x,y: x + y,lst)#output is 113


max_find = lambda a,b: a if (a > b) else b 

lst = [34, 23, 24, 24, 100]

reduce(max_find, lst) #output 100


filter(lambda num: num%2 == 0, lst)#output 24 24 100

x = [1,2,3]
y = [2,3,4]

zip(x, y)#[(1,2),(2,3),(3,4)]

l = ['a', 'b', 'c']

for (count,item) in enumerate(l):
    print count
    print item


l = [True, True, False, False]

any(l)

#complex returns a complex number with the value real + image * ig
complex(2, 3)#2+3j

complex('10+2j')#10+2j