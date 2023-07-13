# Decorator is used to modify a function without effecting the function
# wrap is used to coping the function that is decorated not to lose 
# its name,docstring,data,etc.

from functools import wraps

def myFun(x,y):
    """Does some division math"""
    return x/y

print('')
print('Before using decorator')
print('x(5)/y(10) > ',myFun(5,10))
print('')

def working(fn):                        # Decorator
    
    def inner(x,y):

        if x < y:
            x,y = y,x
        return fn(x,y)
    
    return inner

result = working(myFun)
print('After using decorator')
print('x(5)/y(10) > ',result(5,10))
print('')

print('Before using Decorator with Wrap')
print(result.__name__)
print(result.__doc__)
print('')

def useWrap(fn):

    @wraps(fn)
    def inner(x,y):

        if x<y:
            x,y = y,x
        return fn(x,y)
    
    return inner

resultW = useWrap(myFun)
print('After using decorator with Wrap')
print('x(5)/y(10) > ',resultW(5,10))
print('')
print(resultW.__name__)
print(resultW.__doc__)
print('')