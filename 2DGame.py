# Only use if and while

import secrets

print('\n________ WELCOME TO THE GAME ________\n')

while True:
    print('1) Read the Rules')
    print('2) Play the Game')
    userIn = int(input('Choose > '))
    print('')

    if userIn == 1:
        print('Username must have more than 2 words.')
        print('Age must be greater than 18.')
        print("User's Show Money must have at least 5000$.")
        print('2D Lottery number is between 0 and 100\n')

    elif userIn == 2:
        
        while True:
            uName = input('Enter username > ')
            uAge = int(input('Enter age      > '))
            print('')

            if len(uName) > 2 and uAge > 17:
                break

            else:
                print('Plz... read the rule again.')
                print('Username must have more than 2 words.')
                print('Age must be greater than 18.\n')

        while True:
            showMoney = int(input('Enter Show Money > '))
            print('')

            if showMoney > 4999:
                break

            else:
                print('Plz... read the rule again.')
                print("User's Show Money must have at least 5000$.\n")
        
        srand = secrets.SystemRandom()
        lotNumber = srand.randint(1,99)
        
        while True:
            
            if showMoney == 0:
                print('Sorry... You have no money and cannot play the game!\n')
                break
            
            else:
                print('Your Money : {}$\n'.format(showMoney))
                lotMoney = int(input('Enter money to bet > '))
                luckyDraw = int(input('Enter number       > '))
                print('')

                if luckyDraw > 0 and luckyDraw < 100 and lotMoney <= showMoney:
                
                    showMoney -= lotMoney

                    if luckyDraw == lotNumber:
                        print('Congratulation! You have won {}$'.format(lotMoney*5))
                        showMoney = showMoney + (lotMoney*5)
                    
                    else:
                        print('Sorry... The number is not match.\n')    

                else:
                    print('Plz... read the rule again.')
                    print('Lot money must not greater than Show Money.')
                    print('2D Lottery number is between 0 and 99\n')    

    else:
        print('Enter only mentioned numbers.\n')