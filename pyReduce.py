# reduce(fun,iterable)
# Needs to import functools module
# fun = fun of giving a value that is wanted
# reduce() return one value only.

from functools import reduce

list = [1,2,3,4,5,6]
result = reduce(lambda a,b: a+b, list)

print('')
print('reduce()')
print('')

print('The numbers in a list              > ',end='')
for i in list:
    print(' {} '.format(i),end='')
print('')

print('The sum of all numbers in the list > ',result)
print('Type > {}'.format(type(result)))
print('')

# own implemented fun as the sames as reduce()

def mySum(x,y):
    return x+y

def myReduce(fn,seq):
    
    first = seq[0]

    for i in seq[1:]:
        first = fn(first,i)

    return first

print('Sum by own implemented reduce() > ',myReduce(mySum,list)) 
print('')

min = reduce(lambda a,b: a if a<b else b,list)
print('Minimun value in the List > ',min)
print('')

max = reduce(lambda a,b: a if a>b else b,list)
print('Maximun value in the List > ',max)
print('')

charList = ['L','o','v','e',' ','i','s',' ','R','e','d']
print('The list of char  > {}'.format(charList))
print('')

reStr = reduce(lambda a,b: a+b, charList)
print('The result string > {}'.format(reStr))