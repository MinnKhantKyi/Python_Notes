db = {}
filename = 'Content.txt'

def readFileToDict():

    with open(filename, 'r') as readFile:

        global db
        i = 0
        for line in readFile:
            accList = line.split(' ')
            remove = accList[3]
            accList[3] = remove.strip()
            db.update({i:{'u_name':accList[0],'password':accList[1],
                         'email':accList[2],'phone':accList[3]}})
            i += 1

def checkUser(username):

    length = len(db)
    for i in range(length):
        if db[i]["u_name"] == username:
            return i
    return -1

def appendToFile(username,password,email,phone):

    with open(filename,'a') as appendFile:
        appendFile.write('{} {} {} {}\n'.format(username,password,email,phone))

def register():

    print('\nRegister Account')
    
    while True:
        u_name = input('Enter username     > ')
        
        if u_name.find(" "):
            username = u_name.replace(" ","_")
        else:
            username = u_name

        result = checkUser(username)

        if result != -1:
            print('\nUsername already registered!')
        else:
             break
    
    while True:
        password = input('Enter passwrod     > ')
        confirmPass = input('Confirm password   > ')

        if confirmPass == password:
            break
        else:
            print('\nPasswords must be matched.')
    
    email = input('Enter email        > ')
    phone = int(input('Enter phone number > '))
    appendToFile(username,password,email,phone)
    print('\nRegisteration Successful!')
    main_Menu()
    
def logIn():
    
    print('\nLog In Account')
    
    accIndex = 0
    while True:
        lusername = input('Enter username > ')
    
        if lusername.find(" "):
            username = lusername.replace(" ","_")
        else:
            username = lusername
    
        accIndex = checkUser(username)

        if accIndex != -1:
            break
        else:
            print('\nInvalid Username!')
    
    while True:
        lpassword = input('Enter password > ')

        if lpassword == db[accIndex]["password"]:
            profile(accIndex)
        else:
            print('\nInvalid Password! Try again...')

def profile(acc_index):

    print('\nWelocome!')
    print('Username : {} , Gmail : {} , Phone : {}\n'
          .format(db[acc_index]["u_name"],
                  db[acc_index]["email"],db[acc_index]["phone"]))
    
    while True:
        exit = int(input('Press 1 to exit. > '))

        if exit == 1:
            break
        else:
            print('\nInvalid Number!')

    main_Menu()

def main_Menu():

    readFileToDict()

    print('')
    print('1) Register')
    print('2) Log In')
    print('3) Exit')
    fun = int(input('Enter No. > '))

    if fun == 1:
        register()
    
    elif fun == 2:
        logIn()

    elif fun == 3:
        print('')
        exit(1)

    else:
        print('\n Invalid Number!')
        main_Menu()

if __name__ == '__main__':
    
    while True:
        main_Menu()