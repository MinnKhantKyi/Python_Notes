def matchVal(bi):

    match bi:
        case '0000':
            return '0'
        case '0001':
            return '1'
        case '0010':
            return '2'
        case '0011':
            return '3'
        case '0100':
            return '4'
        case '0101':
            return '5'
        case '0110':
            return '6'
        case '0111':
            return '7'
        case '1000':
            return '8'
        case '1001':
            return '9'
        case '1010':
            return 'A'
        case '1011':
            return 'B'
        case '1100':
            return 'C'
        case '1101':
            return 'D'
        case '1110':
            return 'E'
        case '1111':
            return 'F'
        
def biToHex(bi):

    l = list(bi)
    counter = 0
    hexString = ''
    word = ''

    for i in range(len(l)):

        word = word + l[i]
        counter = counter + 1

        if counter == 4:
            hexString = hexString + str(matchVal(word)) + ' '
            word = ''
            counter = 0

    return hexString

def modRemainder(r):

    match r:
        case '10':
            return 'A'
        case '11':
            return 'B'
        case '12':
            return 'C'
        case '13':
            return 'D'
        case '14':
            return 'E'
        case '15':
            return 'F'
        case r:
            return r

def deciToHex(deci):

    n = deci
    l = list()
    hexString = ''

    while n != 0:
        remainder = n % 16
        modRe = modRemainder(remainder)
        l.append(modRe)
        n = n // 16
    
    l.reverse()

    for i in range(len(l)):
        hexString += str(l[i])

    return hexString



while True:
    print('\nBinary/Decimal/Octal To Hexa Converter')
    print('1) Binary to Hexa')
    print('2) Decimal to Hexa')
    print('3) Octal to Hexa')
    print('4) Exit')
    choose = int(input('Choose > '))

    if choose == 1:
        while True:
            print('\nConverting Binary to Hexa')
            print('Enter -1 to Main Menu')
            print('')
            biString = input('Enter Binary   > ')

            if biString == '-1':
                break
            else:
                convertedOctal = biToHex(biString)
                print('Hexa number    > {}'.format(convertedOctal))

    elif choose == 2:
        while True:
            print('\nConverting Decimal to Hexa')
            print('Enter -1 to Main Menu')
            print('')
            deciString = int(input('Enter Decimal > '))

            if deciString == -1:
                break
            else:
                convertedOctal = deciToHex(deciString)
                print('Hexa number   > {}'.format(convertedOctal))

    elif choose == 3:
        while True:
            print('\nConverting Octal to Hexa')
            print('Enter -1 to Main Menu')
            print('')
            octString = input('Enter Octal > ')

            if octString == '-1':
                break
            else:
                convertedOctal = '0'
                print('Hexa number > {}'.format(convertedOctal))

    elif choose == 4:
        break
    
    else:
        print('Enter only mentioned numbers.\n')