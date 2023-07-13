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
    
    u_name = ''
    
    while True:
        print('Enter -1 to quit')
        u_name = input('Enter username     > ')
        
        if u_name == '-1':
            break

        if u_name.find(" "):
            username = u_name.replace(" ","_")
        else:
            username = u_name

        result = checkUser(username)

        if result != -1:
            print('\nUsername already registered!')
        else:
            break
    
    if u_name != '-1':
        
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
    print('Enter -1 to quit')
    
    accIndex = 0
    lusername = ''

    while True:
        lusername = input('Enter username > ')

        if lusername == '-1':
            break

        if lusername.find(" "):
            username = lusername.replace(" ","_")
        else:
            username = lusername
    
        accIndex = checkUser(username)

        if accIndex != -1:
            break
        else:
            print('\nInvalid Username!')
    
    if lusername != '-1':

        while True:
            lpassword = input('Enter password > ')

            if lpassword == db[accIndex]["password"]:
                break
            else:
                print('\nInvalid Password! Try again...')

        profile(accIndex)

def profile(acc_index):

    print('\nWelocome!')
    print('Username : {} , E-mail : {} , Phone : {}\n'
          .format(db[acc_index]["u_name"],db[acc_index]["email"],
                  db[acc_index]["phone"]))
    
    while True:
        print('1) Change Password')
        print('2) Change Email')
        print('3) Phone number')
        print('4) Exit')
        option = input('Enter > ')

        if option == '1':
            changePass(acc_index)
            break
        
        elif option == '2':
            changeMail(acc_index)
            break
        
        elif option == '3':
            changePhoneNo(acc_index)
            break
        
        elif option == '4':
            break

        else:
            print('\n Invalid Number!')

    main_Menu()

def changePass(acc_index):

    print('\nChange Password')
    print('Enter -1 to quit')

    oldPass = ''

    while True:
        oldPass = input('Old password         > ')

        if oldPass == '-1':
            break
        
        if oldPass == db[acc_index]["password"]:
            break
        else:
            print('Invalid Old password!\n')
    
    if oldPass != '-1':

        while True:
            newPass = input('Enter new password   > ')
            conPass = input('Confirm new password > ')

            if newPass == conPass:
                db[acc_index]["password"] = conPass
                print('Password updated!')
                break
            else:
                print('Passwords must be matched!\n')
    
    updateFile()
    profile(acc_index)

def changeMail(acc_index):

    print('\nChange E-mail')
    print('Enter -1 to quit')

    password = ''

    while True:
        password = input('Enter password to change mail > ')
        
        if password == '-1':
            break

        if password == db[acc_index]["password"]:
            newMail = input('Enter new Mail                > ')
            db[acc_index]["email"] = newMail
            print('E-mail updated!')
            break
        else:
            print('Invalid password!\n')

    updateFile()
    profile(acc_index)

def changePhoneNo(acc_index):

    print('\nChange Phone Number')
    print('Enter -1 to quit')

    password = ''

    while True:
        password = input('Enter password to change phone > ')

        if password == '-1':
            break
        
        if password == db[acc_index]["password"]:
            newPh = input('Enter new Phone                > ')
            db[acc_index]["phone"] = newPh
            print('Phone number updated!')
            break
        else:
            print('Invalid password!\n')

    updateFile()
    profile(acc_index)

def updateFile():
    
    with open(filename, 'w') as file:

        for i in range(len(db)):
            file.write('{} {} {} {}\n'.format(db[i]["u_name"],
                db[i]["password"],db[i]["email"],
                db[i]["phone"]))        

def main_Menu():

    readFileToDict()

    print('')
    print('1) Register')
    print('2) Log In')
    print('3) Exit')
    fun = input('Enter No. > ')

    if fun == '1':
        register()
    
    elif fun == '2':
        logIn()

    elif fun == '3':
        print('')
        exit(1)

    else:
        print('\n Invalid Number!')
        main_Menu()

if __name__ == '__main__':
    
    while True:
        main_Menu()