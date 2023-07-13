a = 10
b = 20
f = 1.12345
name = 'Jarvic'
test = 'O'

print('The value of a is {} and b is {}'.format(a,b))
print('Float Data with 3 point > %.3f' %f)
print('Hello {}, welcome from Python Test {}.'.format(name,test))

print('The value of a is {1} and b is {0}'.format(b,a))
print('Float Data with 5 point > %f' %f)
print('Hello {nameOne}, welcome from {testOne}'.format(nameOne = 'Dean', testOne = 'Python keyword argument'))

data = input('Please enter some integer data > ')
print('Data > {}'.format(data))

# input() fun take input from user as string.
# In this case, dataF receive string type data, so it can't be use with %f format.
dataF = input('Plz enter floating point > ')
# print('Data > %.3f' %dataF) will error
print(' Data > {}'.format(dataF))