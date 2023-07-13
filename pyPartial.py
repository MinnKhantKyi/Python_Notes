# Partial() = used to reduce parameters
# Need to import functools module

from functools import partial

def myFunOne(x,y,z):
    print('{} {} {}'.format(x,y,z))

pFn = partial(myFunOne,10)           # pFn(10,y,z) = myFunOne(10,y,z) 
pFn(20,30)
print('')

def myFunTwo(x,y,*args,x1,y1,**kwargs):
    print('x      > ',x)
    print('y      > ',y)
    print('args   > ',args)
    print('x1     > ',x1)
    print('y1     > ',y1)
    print('kwargs > ',kwargs)

pFn = partial(myFunTwo,10,x1='test')        # 10 is x in myFunTwo
pFn(20,30,40,y1='hello',a=10,b=20,c=30)
print('')

def pow(base,exponent):
    return base**exponent

sq = partial(pow,exponent=2)
print('Square of 4 by partial > ',sq(4))
print('')

cube = partial(pow,exponent=3)
print('Square of 5 by partial > ',cube(5))
print('')