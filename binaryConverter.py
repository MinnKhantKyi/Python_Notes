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
    lenOfStr = len(str)

    for i in range(lenOfStr):
        word = str[i]
        biWord = ' ' + hexToBi(word)
        biString += biWord
    
    return biString

# Octal = Binary

ob0 = '000'
ob1 = '001'
ob2 = '010'
ob3 = '011'
ob4 = '100'
ob5 = '101'
ob6 = '110'
ob7 = '111'

def OctToBi(octal):

    match octal:
        case '0':
            return ob0
        case '1':
            return ob1
        case '2':
            return ob2
        case '3':
            return ob3
        case '4':
            return ob4
        case '5':
            return ob5
        case '6':
            return ob6
        case '7':
            return ob7

def convertOctStr(str):

    biString = ''
    lenOfStr = len(str)

    for i in range(lenOfStr):
        word = str[i]
        biWord = ' ' + OctToBi(word)
        biString += biWord

    return biString

def deciToBi(deci):

    n = deci
    l = list()
    biString = ''

    while n != 0:
        r = n % 2
        l.append(r)
        n = n // 2

    l.reverse()

    for i in range(len(l)):
        biString += str(l[i])

    return biString

while True:
    print('\nHexa/Octal/Deci To Binary Converter')
    print('1) Hexa to Binary')
    print('2) Octal to Binary')
    print('3) Deci to Bianry')
    print('4) Exit')
    choose = int(input('Choose > '))

    if choose == 1:
        while True:
            print('\nConverting Hexadecimal to Binary')
            print('Enter -1 to Main Menu')
            print('')
            hexString = input('Enter hexadecimal > ')
            
            if hexString == '-1':
                break
            else:
                convertedBinary = convertHexStr(hexString)
                print('Binary number     > ' + convertedBinary)
    
    elif choose == 2:
        while True:
            print('\nConverting Octal to Binary')
            print('Enter -1 to Main Menu')
            print('')
            octString = input('Enter octal   > ')

            if octString == '-1':
                break
            else:
                convertedBinary = convertOctStr(octString)
                print('Binary number > ' + convertedBinary)

    elif choose == 3:
        while True:
            print('\nConverting Deciamal to Binary')
            print('Enter -1 to Main Menu')
            print('')
            deci = int(input('Enter decimal > '))

            if deci == -1:
                break
            else:
                convertedBinary = deciToBi(deci)
                print('Binary number > {}' .format(convertedBinary))
    
    elif choose == 4:
        break

    else:
        print('Enter only mentioned numbers.\n')