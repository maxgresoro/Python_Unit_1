import sys
import time
import getpass


characters = []
lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
number = ["1","2","3","4","5","6","7","8","9","0"]


password = getpass.getpass('Enter 4 character password :')
starttime = time.time()

#Creates array with most keyboard characters
for i in range(len(lower)):
    characters.append(lower[i])
for i in range(len(upper)):
    characters.append(upper[i])
for i in range(len(number)):
    characters.append(number[i])


found = False

for a in range(len(characters)):
    for b in range(len(characters)):
        for c in range(len(characters)):
            for d in range(len(characters)):
                if (characters[a] + characters[b] + characters[c] + characters[d] == password):
                    print ("Password is",characters[a] + characters[b] + characters[c] + characters[d])
                    stoptime = time.time()
                    print ("Password was cracked in",round(stoptime-starttime,2),"seconds")
                    found = True
if (found):
    sys.exit()


