#integer numbers/folating point numbers

#in python2 a == 1, in python3 a == 1.5
var div = 3/2
#from __future__ import division, the a should be 1.5

var power = 4 **5


#Strings
#in python2 it is print '123'
#in python3 
print('123')
len('123 321')
s = '123'
var c1 = s[0]
var c2 = s[1:]
var c3 = s[:3]
var c4 = s[:]
var c5 = s[:-1]
var c5 = s[::2]#wrap all content with 2 times frequency

var s = s + ' concatenate me'

letter = 'z'
letter = letter * 10#letter == 'zzzzzzzzzz


#print formattubg
print('this is a string')
x = 'String'
print('place my variable here : %s' %(x))

print('floating point number : %1.2f' %(13.145))
print('convert to string %r'%(123))
print('first: %s, second %s, third: %s' %('hi','tw','3'))
print('fisrt: {x} second:{y} third:{z}'.format(x ='1',z='3','y'='2'))


#list

my_list = [1,2,3]
my_list = ['string',1,123.22]
len(my_list)

my_list = ['one','two','three',4,5]
my_list[0] == 'one'
my_list[:3]
my_list[1:]
my_list = my_list + ['new_item']
my_list = my_list * 2
my_list.append('append_me')

#nesting structure => matrix, my_list.sort remove pop pop(index) reverse.........



#dictionaries

my_dict = {'key1':'value1','key2':'value2'}
my_dict['key1']
my_dict.keys()
my_dict.values()
my_dict.items()


#tuples tuples object doesn't support item assignment
my_tuple = (1,2,3)
my_tuple.index(2)
my_tuple.count(2)


#files
f = open('text.txt')
f.read()#cursor will move to the end of the file
f.seek(9)
f.readlines()

%%writefile new.txt
first line
second line

for line in open('new.txt'):
    print(line)



#set sets only concern the unique elements

x = set()
x.add(1)
x.add(1)#{1}
list_x = [1,2,3,4,1,2,3,4]
x.add(list_x)




