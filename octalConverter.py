def matchVal(val):

    match val:
        case '000':
            return 0
        case '001':
            return 1
        case '010':
            return 2
        case '011':
            return 3
        case '100':
            return 4
        case '101':
            return 5
        case '110':
            return 6
        case '111':
            return 7

def biToOctal(bi):
    
    l = list(bi)
    counter = 0
    octStr = ''
    word = ''
    
    for i in range(len(l)):
        
        word = word + l[i]
        counter = counter + 1

        if counter == 3:
            octStr = octStr + str(matchVal(word)) + ' '
            word = ''
            counter = 0

    return octStr

def deciToOctal(deci):

    n = deci
    l = list()
    octStr = ''

    while n != 0:
        remainder = n % 8
        l.append(remainder)
        n = n // 8

    l.reverse()

    for i in range(len(l)):
        octStr += str(l[i])

    return octStr

# Hexa = Binary
hb0 = '0000'
hb1 = '0001'
hb2 = '0010'
hb3 = '0011'
hb4 = '0100'
hb5 = '0101'
hb6 = '0110'
hb7 = '0111'
hb8 = '1000'
hb9 = '1001'
hbA = '1010'
hbB = '1011'
hbC = '1100'
hbD = '1101'
hbE = '1110'
hbF = '1111'

def hexToBi(hex):

    match hex:
        case '0':
            return hb0
        case '1':
            return hb1
        case '2':
            return hb2
        case '3':
            return hb3
        case '4':
            return hb4
        case '5':
            return hb5
        case '6':
            return hb6
        case '7':
            return hb7
        case '8':
            return hb8
        case '9':
            return hb9
        case 'A':
            return hbA
        case 'B':
            return hbB
        case 'C':
            return hbC
        case 'D':
            return hbD
        case 'E':
            return hbE
        case 'F':
            return hbF
        
def convertHexStr(str):

    biString = ''
    biword = ''
    lenOfStr = len(str)

    for i in range(lenOfStr):
        word = str[i]
        biWord = hexToBi(word)
        biString += biWord
    
    return biString

def modifyBiStr(bi):

    modBi = ''
    l = list(bi)
    length = len(l)
    l.reverse()

    if (length % 3) == 1:
        l.append('0')
        l.append('0')

    elif (length % 3) == 2:
        l.append('0')

    l.reverse()
    
    for i in range(len(l)):
        modBi += str(l[i])

    return modBi    

def hexToOctal(hex):
    
    biStr = convertHexStr(hex)
    modString = modifyBiStr(biStr)
    octStr = biToOctal(modString)

    return octStr

while True:
    print('\nBinary/Decimal/Hexa To Octal Converter')
    print('1) Binary to Octal')
    print('2) Decimal to Octal')
    print('3) Hexa to Octal')
    choose = int(input('Choose > '))

    if choose == 1:
        while True:
            print('\nConverting Binary to Octal')
            print('Enter -1 to Main Menu')
            print('')
            biString = input('Enter Binary   > ')

            if biString == '-1':
                break
            else:
                convertedOctal = biToOctal(biString)
                print('Octal number   > {}'.format(convertedOctal))

    elif choose == 2:
        while True:
            print('\nConverting Decimal to Octal')
            print('Enter -1 to Main Menu')
            print('')
            deciString = int(input('Enter Decimal > '))

            if deciString == -1:
                break
            else:
                convertedOctal = deciToOctal(deciString)
                print('Octal number  > {}'.format(convertedOctal))

    elif choose == 3:
        while True:
            print('\nConverting Hexa to Octal')
            print('Enter -1 to Main Menu')
            print('')
            hexString = input('Enter Hexadecimal > ')

            if hexString == '-1':
                break
            else:
                convertedOctal = hexToOctal(hexString)
                print('Octal number      > {}'.format(convertedOctal))
    
    else:
        print('Enter only mentioned numbers.\n')