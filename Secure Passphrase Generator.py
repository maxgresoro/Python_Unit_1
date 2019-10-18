#  Max Gresoro - IT075 Sierra College
#  Assingment to create passphrase using 4 random words
#  random words will be selected from an external text file


import random, string

print("This program will generate a random passphrase of 4 random words from a list of common words in English");
print();

passphrase = ''
wordlist = ['random','answer','betray','tomorrow','easy','number','energy','sample','driver','pepper','survive','doctor','neighbor','zebra','bathroom','function','office','equal','river','football','ocean','silver','valley','cotton','honey','river','week']
random.shuffle(wordlist)  #  randomly shuffle the words in the list

passphrase = ''
for i in range(0,4):
    pointer = random.randint(0,len(wordlist));  # select a random word from the list
    passphrase += wordlist[pointer];  # append the random word to the passphrase

print("Your random generated passphrase is : ",passphrase)  # print the passphrase
print()

print("However per IT policy we must have numbers and special characters")
print("included in your passphrase.  We will make several character substitutions")
print("to make the passphrase more secure")

passphrase = list(passphrase)  # convert string to a list for character substitution

for i in range(0,len(passphrase)):  # replace certain lowercase letters with special characters
    if passphrase[i] == 's':
        passphrase[i] = '$'
    elif passphrase[i] == 'o':
        passphrase[i] = '0'
    elif passphrase[i] == 'a':
        passphrase[i] = '@'
    elif passphrase[i] == 'p':
        passphrase[i] = '%'
passphrase = ''.join(passphrase)  # convert list back to string

print()
print("Your super secure passphrase is now : ",passphrase)
print("So easy to remember yes?")
print()
