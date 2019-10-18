#  Max Gresoro - IT075 Sierra College
#  Assingment to create a random 4 character password

import random, string

print()
print("This program will generate a random password of 4 characters and numbers")
print()

password = ''  # blank out password variable

for i in range(0,4):
    chartype = random.randint(0,2)
    if chartype == 0:
        password = password + random.choice(string.digits)  # randomly select a number
    elif chartype == 1:
        password = password + random.choice(string.ascii_lowercase)  # randomly select a lowercase letter
    elif chartype == 2:
        password += random.choice(string.ascii_uppercase)  # randomly select a uppercase letter
    else:
        break
print("Random generated password is : ",password)
print()
