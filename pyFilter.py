# filter(func,iterable)
# func = function that filter required data and return true or false
# iterable = data that want to filter
# If func return true, filter() will return the data
# If func return false, filter() will return no data
# The received data will get the return values in list[]

def VowelFilter(alphabet):
    
    vowel = ['a','e','i','o','u']

    if alphabet in vowel:
        return True
    else:
        False

alphabet = ['a','b','c','d','e','a','f','g','h','i','a','j','o','u','i']
strAlpha = "Love grow where my rosemary goes"

alphabetFilter = filter(VowelFilter,alphabet)
stringFilter = filter(VowelFilter,strAlpha)

print('')
print('Filter() in Python')
print('')

print('Before filtering vowel:')
print('Alphabet List > ',end='')
for i in alphabet:
    print(' {} '.format(i),end='')
print('')
print('String        > ',strAlpha)
print('')

print('After filtering vowel:')
print('Alphabet List > ',end='')
for i in alphabetFilter:
    print(' {} '.format(i),end='')
print('')
print('String        > ',end='')
for i in stringFilter:
    print(' {} '.format(i),end='')
print('')