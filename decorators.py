'''decorators
decorators can be thought of as functions which modify the functionality of another function. 
They help to make code shorter.
'''

s = 'this is a global variable'

def func():
    print(locals())

print(globals().keys())


def hello(name='Jose'):

    print('the hello function has been excuted')

    def greet():
        return 'this is inside greet function'

    def welcome():
        return 'this is inside welcome function'

    if name == 'Jose':
        return greet
    else:
        return welcome


def new_decorator(func):

    def wrap_func():

        print('before excuting the fuc')
        func()
        print('code here will execute after func')
    
    return wrap_func

@new_decorator
def func_need_decorator():
    print('this is function needs a decorator')

func_needs_decorator = new_decorator(func_need_decorator)

func_need_decorator()
