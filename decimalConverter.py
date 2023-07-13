def biToDeci(bi):
    
    sum = 0
    l = list(bi)

    for i in range(len(l)):
        power = len(l) - (i+1)
        sum = sum + (int(l[i])*2**power)

    return sum

def octToDeci(oct):

    sum = 0
    l = list(oct)

    for i in range(len(l)):
        power = len(l) - (i+1)
        sum = sum + (int(l[i])*8**power)

    return sum

def swapValue(val):
    
    match val:
        case 'A':
            return 10
        case 'B':
            return 11
        case 'C':
            return 12
        case 'D':
            return 13
        case 'E':
            return 14
        case 'F':
            return 15
        case val:
            return val

def hexToDeci(hex):

    sum = 0
    l = list(hex)

    for i in range(len(l)):
        power = len(l) - (i+1)
        l[i] = swapValue(l[i])
        sum = sum + (int(l[i])*16**power)

    return sum

while True:
    print('\nBinary/Octal/Hexa To Decimal Converter')
    print('1) Binary to Decimal')
    print('2) Octal to Decimal')
    print('3) Hexa to Decimal')
    choose = int(input('Choose > '))

    if choose == 1:
        while True:
            print('\nConverting Binary to Decimal')
            print('Enter -1 to Main Menu')
            print('')
            biString = input('Enter Binary   > ')

            if biString == '-1':
                break
            else:
                convertedDecimal = biToDeci(biString)
                print('Decimal number > {}'.format(convertedDecimal))

    elif choose == 2:
        while True:
            print('\nConverting Octal to Decimal')
            print('Enter -1 to Main Menu')
            print('')
            octString = input('Enter Octal    > ')

            if octString == '-1':
                break
            else:
                convertedDecimal = octToDeci(octString)
                print('Decimal number > {}'.format(convertedDecimal))

    elif choose == 3:
        while True:
            print('\nConverting Hexa to Decimal')
            print('Enter -1 to Main Menu')
            print('')
            hexString = input('Enter Hexadecimal > ')

            if hexString == '-1':
                break
            else:
                convertedDecimal = hexToDeci(hexString)
                print('Decimal number    > {}'.format(convertedDecimal))
    
    else:
        print('Enter only mentioned numbers.\n')