#  Max Gresoro - IT 075 Sierra College
# Password Manager Project

# This week, you will explore (use) Sweigart's first project, add features (modify) like simple encryption and password generation to the project, 
# and design a feature (create) of your own choosing for your quasi-secure password manager.

# To start, review the Password Locker project in Chapter 6 in ATBS.  You should recreate the code and add your comments noting and predicting functionality.

# Next, revisit your Python Password Generator and Encryption projects.  Using your Password Locker starter code, see if you can reuse and/or modify your code to:

# Encrypt and decrypt the passwords saved in the dictionary.  A master password is required for decryption.  How will you handle the conditionals and exception handlers 
# for incorrect passwords?  Create a "menu" consisting of nicely formatted strings that provide the user options to add new passwords to the dictionary, retrieve passwords, 
# and generate random passwords that are "strong" according to XKCD.



import  getpass, os, random, string, sys, pyperclip, time

CHARACTERS = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_')  # string of standard ascii characters

#  the following words will be used in the password generator functions
ARTICLES = ['a','the']
COLOR = ['red','orange','yellow','green','blue','purple','brown','magenta','tan','cyan','olive','maroon','navy','silver','violet','pink','black','white','grey']
NOUNS = ['area','book','business','case','child','company','country','day','eye','fact','family','government','group','hand','home','job','life','lot','man','money','month','mother','mr','night','number','part','people','place','point','problem','program','question','right','room','school','state','story','student','study','system','thing','time','water','way','week','woman','word','work','world','year']
VERBS = ['ask','be','become','begin','call','can','come','could','do','feel','find','get','give','go','have','hear','help','keep','know','leave','let','like','live','look','make','may','mean','might','move','need','play','put','run','say','see','seem','should','show','start','take','talk','tell','think','try','turn','use','want','will','work','would']
ADVERBS = ['angrily','anxiously','awkwardly','badly','beautifully','calmly','carefully','carelessly','cautiously','cheerfully','clearly','closely','correctly','deliberately','eagerly','easily','enthusiastically','fast','fondly','frankly','frantically','gently','happily','healthily','hurriedly','innocently','naturally','neatly','nervously','noisily','obediently','patiently','perfectly','politely','powerfully','quickly','reluctantly','repeatedly','safely','shyly','silently','slowly','softly','stupidly','suspiciously','well']
ADJECTIVES =['able','bad','best','better','big','black','certain','clear','different','early','easy','economic','federal','free','full','good','great','hard','high','human','important','international','large','late','little','local','long','low','major','military','national','new','old','only','other','political','possible','public','real','recent','right','small','social','special','strong','sure','true','white','whole','young']

# initialize the password dictionary
PASSWORDDICT = {}   

# try to access the password file.  if not available try to create a new one
try:
    FILE = open('C:\\Temp\\passey.txt', 'r')
    PASSWORDDICT = eval(FILE.read())
    FILE.close()
except:
    try:
        print('Password file not found.  Attempting to create')
        os.mkdir('C:\\Temp\\')
        FILE = open('C:\\Temp\\passey.txt', 'w+')
        PASSWORDDICT = eval(FILE.read())
        FILE.close()
        print('Password file created sussesfully in C:\\Temp')
        time.sleep(3)
    except:
        print('Password file cannot be created.  Nothing created here can be saved')
        time.sleep(3)

        
# **********************************  DEFINE ALL FUNCTIONS BELOW  **********************************

# the following function is used to generate the user menu
def menu():
        cls()
        strs = ('************ MAIN MENU ************\n'
                '1 - Store password for an account\n'
                '2 - Retrieve password for an account\n'
                '3 - Delete account information\n'                
                '4 - Generate random password\n'
                '5 - QUIT\n')
        print(strs)
        choice = input('Select a function to perform: ')
        return int(choice)
    
# the following function is used to get a password from the user
def getpassword():
    try: 
        p1 = getpass.getpass('Type password ')
        p2 = getpass.getpass('Type password again to confirm ')
    except: 
        print('Invalid Password, return to Menu')
        input('Press enter to continue')
        return None
    if p1 == '':
        print('** No Password Entered - Aborting Operation **')
        return None
    elif p1 == p2:
        return(p1)
    else:
        print('** Passwords do not match - Aborting Operation **')
        time.sleep(5)
        return None

# the following function is used to get a pin number from the user
def getpin():
    try: 
        p1 = int(getpass.getpass('Type PIN '))
        p2 = int(getpass.getpass('Type PIN again to confirm '))
    except: 
        print('** Invalid Entry - Operation Has Been Aborted **')
        time.sleep(5)
        return None
    if p1 == p2:
        return(int(p1))
    else:
        print('PIN''s do not match nothing returned')
        print('Returning to Main Menu')
        time.sleep(5)
        return None

# the following function is used to get the account name from the user
def getaccount():
    account = input('Enter account name: ')
    if account == '':
        return None
    else:
        return account

# the following function looks up the account name from the password dictionary
def getaccountpassword(account):
    return PASSWORDDICT.get(account)


# the following function puts a account name and password into the password dictionary
def putaccountpassword(account,password):
    PASSWORDDICT[account] = password
    return
    

# the following function is used to encrypt a string using the character substitution method
def encrypt(string_to_encrypt,pin):
    list_to_encrypt = list(string_to_encrypt)
    encrypted_list = []#list_to_encrypt
    
    char_list = list(CHARACTERS)
    char_list_reverse = char_list
    char_list_reverse.reverse()
    #print('char_list_reverse: ',char_list_reverse)
    
    string_split = pin % len(char_list_reverse)
    cipher_key_list = char_list_reverse[string_split:] + char_list_reverse[:string_split]
    #print('cipher_key_list:   ',cipher_key_list)
    
    for i in range(0,len(list_to_encrypt)):
        encrypted_list.append(cipher_key_list[char_list.index(list_to_encrypt[i])])
    encyrpted_string = ''.join(encrypted_list)  # convert list _to_ string
    #print('The encrypted_list message is:',encyrpted_string)  # print string output
    #print()
    return encyrpted_string


# the following function is used to decrypt a password using the reverse character substitution method
def decrypt(string_to_decrypt,pin):
    char_list = list(CHARACTERS)
    char_list_reverse = char_list
    char_list_reverse.reverse()
    list_to_decrypt = list(string_to_decrypt)

    string_split = pin % len(char_list_reverse)
    cipher_key_list = char_list_reverse[string_split:] + char_list_reverse[:string_split]
    
    decrypted_list = []    
    for i in range(0,len(list_to_decrypt)):
        decrypted_list.append(char_list[cipher_key_list.index(list_to_decrypt[i])])
        decyrpted_string = ''.join(decrypted_list)  # convert list to string
    return decyrpted_string

# the following function will print all the account names from the password dictionary
def showaccounts():
    for key, value in PASSWORDDICT.items():
        print(key)
    return None    


# the following function will generate a raondom password from the defined wordlists
def getrandompassword():
    sentence = random.choice(ARTICLES)+random.choice(COLOR)+random.choice(NOUNS)+random.choice(VERBS)+random.choice(ADVERBS)
    sentence = ''.join(sentence)
    #print(sentence)
    return sentence

# the following function will save the password dictionary to an external file
def writepasswordfile(writing):
    try:
        FILE = open('C:\\Temp\\passey.txt', 'w+')
        FILE.write(str(writing))
        FILE.close()
    except:
        print('Something went wrong and the password file cannot be saved')


# the following function will clear the terminal screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    




#  **********************************   START MAIN PROGRAM HERE   **********************************
cls()
print('Welcome to PASSEY - the very insecure password manager')
print('LEGAL DISCLAIMER: Use at your own risk.  Do not use real passwords in this demo program!')
print()

while True:          #loop until break statement
    choice = menu()
    cls()

# the following menu selection will store a new encrypted password for a new or existing account
    if choice == 1:
        cls()
        print('********* STORE PASSWORD FOR ACCOUNT *********')
        print()
        print('The accounts we have in the vault are:')
        showaccounts()
        print()
        print('Type in the account you would like to modify or type in a new account name to add to the vault')
        ACCOUNT = getaccount()
        print('Account is: ', ACCOUNT)
        if ACCOUNT == None:
            print('** Invalid Entry - Operation Has Been Aborted **')
            print()
            time.sleep(5)
            pass
        else:        
            print('Press ENTER to continue')
            randomselect = input('or enter "random" to generate a random password: ')
            if randomselect == 'random':
                PASSWORD = getrandompassword()
            else:
                PASSWORD = getpassword()

            if PASSWORD == None:
                print('** Invalid Entry - Operation Has Been Aborted **')
                print()
                time.sleep(5)
                pass
            else:    
                print('Enter PIN number to encrypt the password with')
                PIN = getpin()
                if PIN == None:
                    print('** Invalid Entry - Operation Has Been Aborted **')
                    print()
                    time.sleep(5)
                    pass
                else:
                    PASSWORDSECURE = encrypt(PASSWORD,PIN)
                    putaccountpassword(ACCOUNT,PASSWORDSECURE)
                    print('The password is now stored in your account')
                    print()
                    time.sleep(5)
        print()        

# the following menu selection will retrieve and decrypt a password for an account in the password dictionary
    elif choice == 2:
        cls()
        print('********* RETRIEVE PASSWORD FOR AN ACCOUNT *********')
        print()
        print('The stored accounts are:')
        showaccounts()
        print()
        ACCOUNT = getaccount()
        
        if ACCOUNT == None:
            print('** Invalid Entry - Operation Has Been Aborted **')
            time.sleep(5)
            pass
        else:
            print('Account is:', ACCOUNT)
            PASS = getaccountpassword(ACCOUNT)
            if PASS == None:
                print('Account password does not exist')
                print('Return to Main Menu')
                print()
                time.sleep(5)
                pass
            else:
                PIN = getpin()
                if PIN == None:
                    print('** Invalid Entry - Operation Has Been Aborted **')
                    time.sleep(5)
                    pass
                else:
                    PLAINPASS = decrypt(PASS,PIN)
                    print('Decrypted password is: ', PLAINPASS)
                    pyperclip.copy(PLAINPASS)
                    print('Password is copied to the clipboard')
                    print()
                    time.sleep(5)

# the following menu selection will delete and account and password from the dictionary
    elif choice == 3:
        cls()
        print('********* DELETE ACCOUNT INFORMATION *********')
        showaccounts()
        ACCOUNT = getaccount()
        
        if ACCOUNT == None:
            print('ERROR:  Invalid account name entered - Returning to Main Menu')
            print()
            time.sleep(5)
            pass
        else:
            print('Enter "yes" to confirm deletion of account ', ACCOUNT)
            print('or press ENTER to abort')
            confirm = input()
            if confirm == 'yes':
                try:
                    PASSWORDDICT.pop(ACCOUNT)
                    print('The entry for %s has been removed' % ACCOUNT)       
                    print()
                    time.sleep(5)
                    pass
                except:
                    print('ERROR:  Something Went Wrong - Returning to Main Menu')
                    print()
                    time.sleep(5)
                    pass
            else:
                print('Operation Aborted - Returning to Main Menu')
                print()
                time.sleep(5)

# the following menu selection will generate a random password and copy it to the clipboard
    elif choice == 4:
        cls()
        print('********* RANDOM PASSWORD GENERATOR *********')
        print()
        RANDOMPASS = getrandompassword()
        print('The random password is: ', RANDOMPASS)
        print()
        pyperclip.copy(RANDOMPASS)
        print('The random password is copied to the clipboard')
        print()
        time.sleep(5)
        pass
 
 # the following menu selection will save the password dictiionary and exit the system   
    elif choice == 5:
        cls()
        print('Saving password file ....')
        writepasswordfile(PASSWORDDICT)
        print('Thank you and goodbye')
        time.sleep(5)
        cls()
        break

# the following menu selection is hidden from the menu and is used in debugging purposes
    elif choice == 66:
        cls()
        for k,v in PASSWORDDICT.items():
            print('Account:',k, '--- Password:',v)
        print()
        print(PASSWORDDICT)
        print()
        input('press enter')   

# terminates the program and returns to the terminal 
sys.exit()
