#  Max Gresoro - IT075 Sierra College
#  Chap 5 assingment to write a program that will 
#  encode a message using the Caesar Cipher
#  using a shift value that the user inputs

import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'
plaintext = 'thequickbrownfoxjumpsoverthelazydog'

alphabetlist = list(alphabet)
plaintextlist = list(plaintext)
print('The original message is:',plaintext)
shift = int(input('To encrypt this message enter a shift value 0-25: '))  # request shift value from user

code = alphabetlist[shift:] + alphabetlist[:shift]  #  generate the alpabet code
print('The encryption alphabet is:',''.join(code))

cipherlist = plaintextlist
for i in range(0,len(plaintextlist)):
    cipherlist[i] = code[alphabetlist.index(plaintextlist[i])]  # substitue the letters in the plaintext message using the ciperher alphabet

ciphertext = ''.join(cipherlist)  # convert list to string
print('The encrypted message is:',ciphertext)  # print string output
print()