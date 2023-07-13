print('')
print('iter()')
print('')

list = ['a','b','c','d']
iterator = iter(list)

print('Type > {}'.format(type(iterator)))
print('First time iteration  > {}'.format(next(iterator)))
print('Second time iteration > {}'.format(next(iterator)))
print('Third time iteration  > {}'.format(next(iterator)))
print('Fourth time iteration > {}'.format(next(iterator)))
print('')

print('map()')
print('')

# map iterate number that programmer wanted in a range.
# map(function,range)
# function = generate number that required
# range = range of that number

def fact(n):
    return 1 if n<2 else n*fact(n-1)

result = map(fact,range(6))

print('Type > {}'.format(type(result)))
print('Iteration of map by using for loop ')

for i in result:
    print(i)
print('')

print('zip()')
print('')

# zip return value in a form of tuple if there is two arguments

itr = [1,2,3,4,5]
itr1 = [10,20,30]

result = zip(itr,itr1)

print('Type > {}'.format(type(result)))
print('Iteration of zip by using for loop ')

for i in result:
    print(i)
print('')

# iter, map, zip return one value at one time by using generator
# So, after giving all valuse, they cannot use it again and 
# there are no value because of using generator

print('generator()')
print('')

# generator use yield keyword to return one value at one time.
# After yield, it pauses the process until it is called again.

def myGen(n):
    x = 1
    while x <= n:
        square = x * x
        yield square
        x += 1

result = myGen(10)

print('Type > {}'.format(type(result)))
print('Iteration of zip by using for loop ')

for i in result:
    print(i)