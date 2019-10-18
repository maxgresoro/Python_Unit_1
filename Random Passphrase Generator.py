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
