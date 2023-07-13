# Testing two lists pass to *args
def myFun(a,b,*args):
    print('Positional Arguments > {0} {1}'.format(a,b))
    print('Arbitrary Arguments  > {}'.format(args))

myList = [1,2,3]
myList1 = [4,5,6]

myFun('P1','P2',myList,myList1)

print('')

# High-Order Function with *arg and *kwarg

def myHoFun(fn,*args,**kwargs):
    return fn(*args,**kwargs)

twoValue = myHoFun(lambda x,*,y:x+y,10,y=11)
print('Both arg and kwarg > {}'.format(twoValue))

print('')

argValue = myHoFun(lambda *args:args, 1,2,3,4,5)
print('Only args > {}'.format(argValue))
print(type(argValue))

print('')

kwArgVal = myHoFun(lambda **kwargs:kwargs, a=10,b=20)
print('Only kwargs > {}'.format(kwArgVal))
print(type(kwArgVal))

print('')