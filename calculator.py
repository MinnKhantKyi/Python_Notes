import math

print('Enter 1 for Add')
print('Enter 2 for Subtract')
print('Enter 3 for Multiply')
print('Enter 4 for Divide')
print('Enter 5 for Modulus')
choose = int(input('Enter some number > '))

while True :
    if choose <= 0 or choose > 5:
        print('Plz enter number between 1 and 5 only.')
        choose = int(input('Enter some number > '))
    else:
        break

def add(a,b):
    res = a+b
    return res

def sub(a,b):
    res = a-b
    return res

def multi(a,b):
    res = a*b
    return res

def divide(a,b):
    res = a/b
    return res

def modulus(a,b):
    res = a%b
    return res

def report(a,b,result,sign):
    if sign == 1:
        print('Result : {} + {} = {}'.format(a,b,result))
    elif sign == 2:
        print('Result : {} - {} = {}'.format(a,b,result))
    elif sign == 3:
        print('Result : {} x {} = {}'.format(a,b,result))
    elif sign == 4:
        print('Result : {} / {} = {}'.format(a,b,result))
    else:
        print('Result : {} % {} = {}'.format(a,b,result))    

fData = int(input('Enter first number  > '))
sData = int(input('Enter second number > '))

if choose == 1:
    result = add(fData,sData)
    report(fData,sData,result,choose)
elif choose == 2:
    result = sub(fData,sData)
    report(fData,sData,result,choose)
elif choose == 3:
    result = multi(fData,sData)
    report(fData,sData,result,choose)
elif choose == 4:
    result = divide(fData,sData)
    report(fData,sData,result,choose)
else:
    result = modulus(fData,sData)
    report(fData,sData,result,choose)