#  Max Gresoro - IT075 Sierra College
#  Chap 5 assingment to write a program that will encrypt a message
#  using a randomly generated alphabet key and then decrypt that message
#  using the same key to get back the original message
#  Remove any duplicate letters from the password.
#  Now split the alphabet into two halves The letters up to and including the last letter in the password and the rest of the alphabet.
#  Remove any letters in your password from the two halves of the alphabet.
#  The key is the concatenation of the password (without duplicate letters) followed by the second part of the split alphabet followed by the first part of the alphabet.

import string
import random



plaintext = input('Input a password using all lowercase letters and no spaces:')  # user inputs a message to encrypt

alphabet = 'abcdefghijklmnopqrstuvwxyz'  # build a sting of the alphabet characters
alphabetlist = list(alphabet)  # convert alphabet string to list
key = "".join(random.sample(alphabet,len(alphabet)))  # generate the encyption key by randomizing the alphabet

keylist = list(key)  # convert encryption string to list
dictionary = dict(zip(alphabetlist,keylist))  # generate a dictionary reference the alphabet to the encryption key
revdictionary = dict(zip(keylist,alphabetlist))  # generate a dictionary reference for the reverse lookup

print()  # print blank line for separation
plaintext = input('Input a message to encyrpt using all lowercase letters and no spaces:')  # user inputs a message to encrypt
plainlist = list(plaintext)  # convert string to list
print()



cipherlist = []
for i in range(0,len(plainlist)):  # loop to encrypt each character in the user input message
    cipherlist.append(dictionary.get(plainlist[i],''))  # build the encrypted message using the encryption dictionary

print('The encyrption key is:',key)  #  print the encryption key for reference
ciphertext = ''.join(cipherlist)  # convert list to string
print('The encyrpted message is:',ciphertext)  # show user their encrypted message
print()  # print blank line for separation

plaintext = []  # initialize decryption list
for i in range(0,len(ciphertext)):  # generate loop to decrypt each character in the encrypted message
    plaintext.append(revdictionary.get(cipherlist[i],''))  #  build the decrypted message as a list using the decryption dictionary

decipher = ''.join(plaintext)  # convert decrypted message list to a string

print('The decyrption key is:',key)  # show user the decryption key
print('The decyrpted message is:',decipher)  # show user the decrypted message
print()  # print blank line for separation
