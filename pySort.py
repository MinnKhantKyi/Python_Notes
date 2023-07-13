# sorted() -> sort valuse in Ascending Order

print('')

data = ['c','A','a','B','D']
print('Before sorting           > {}'.format(data))
print('')
print('After sorting            > {}'.format(sorted(data)))
print('')

ls = sorted(data,key=lambda ld: ld.upper())
print('Sort after using upper() > {}'.format(ls))
print('')

di = {'a':300,'c':500,'d':100}
print('Before sorting dictionary  > {}'.format(di))
print('')
sd = sorted(di)
print('Sort dictionary with key   > {}'.format(sd))
print('')
sd = sorted(di,key=lambda i:di[i])
print('Sort dictionary with value > {}'.format(sd))
print('')

a_l = ['Guido','green','team']
print('Before sorting string list   > {}'.format(a_l))
print('')
result = sorted(a_l,key=lambda ac:ac[-1])
print('After sorting with last char > {}'.format(result))
print('')