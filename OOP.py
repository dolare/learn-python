##in python, everthing is object
class Sample(object):
    pass

x = Sample()

type(x)#__main__.Sample

class Dog(object):
    #class object attribute
    species = 'animal'
    
    def __init__(self,breed):
        self.breed = breed


sam = Dog(breed = 'HusKie')


##basically methods are functions defined inside the body of a class


'''inheritance
is a way to form new classes using classes thath have already been defined.
can help us reuse the code
'''


#special methods
class Book(object):
    def __init__(self,title,author,pages):
        print('this is a book')
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "titile: %s, Author: %s, pages: %s" %(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('delete is done')
        