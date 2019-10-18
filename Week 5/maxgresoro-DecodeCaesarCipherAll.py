#  Max Gresoro - IT075 Sierra College
#  Chap 5 assingment to write a program that will attempt to 
#  decode a message that has been encoded using the Caesar Cipher
#  25 iterations of the shifted alphabe will be used so that the user
#  can determine if the output is valid for each decryption attempt

import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'  # standard alphabet
alphabetlist = list(alphabet)  # convert string to list
ciphertext = 'dzeevjfkrlezkvuwffksrcctcls'  # the ciper message to be de coded
cipherlist = list(ciphertext)  # convert list to string

print('The encrypted message is:',ciphertext)


for i in range(1,len(alphabet)):  # setup a loop for all possible combinations of the shifted alphabet
    codelist = alphabetlist[i:] + alphabetlist[:i]  # build the shifted alphabet as a list
    decipherlist = []       # initialize the list to build
    for j in range(0,len(cipherlist)):      # loop to build decrypted message substituting each character in ciphertext
        decipherlist.append(alphabetlist[codelist.index(cipherlist[j])])    # build the decrypted message one character at a time.  use list index function to cross reference character substitution
    deciphertext = ''.join(decipherlist)  # convert list to string
    print('Decryption attempt #',i,'is: ',deciphertext)  # print the decrypted message
