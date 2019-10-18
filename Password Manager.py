import getpass, hashlib, os, random, string, sys


def hash_password(password, salt=None, iterations=100000):
	# Do type checking
	if not type(password) == type("String"):
		raise TypeError("Password should be a string")

	# if no salt is given
	# generate 16 alphanumeric long salt using system random
	if not salt:
		salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))

	# encode to make it compatible with hashlib algorithm
	encoded_password = bytes(password, encoding='utf-8')
	encoded_salt = bytes(salt, encoding='utf-8')

	pass_hash = hashlib.sha3_512(encoded_password+encoded_salt).hexdigest()

	# use iterative hashing
	for _ in range(iterations):
		pass_hash = hashlib.sha3_512(bytes(pass_hash, encoding="utf-8")+encoded_password).hexdigest()

	return (pass_hash, salt)


def validate_password(password, pw_hash_tuple):
	# Do input validation
	if not len(pw_hash_tuple) == 2:
		raise ValueError("pw_hash_tuple should have length 2")

	if not type(password) == type('string'):
		raise TypeError("password should be a string")

	for item in pw_hash_tuple:
		if not type(item) == type("string"):
			raise TypeError("items in pw_hash_tuple should be strings")


	stored_pw_hash = pw_hash_tuple[0]
	stored_pw_salt = pw_hash_tuple[1]

	# compute the hash of guesspassword using the same salt
	user_pw_hash_tuple = hash_password(password, salt=stored_pw_salt)

	# compare the two hashes
	if user_pw_hash_tuple[0] == stored_pw_hash:
		return True
	else:
		return False


currentDirectory = os.getcwd()
print(currentDirectory)
path = "C:\Temp"
os.chdir(path)
print(currentDirectory)

hashtext = open("C:\Temp\hash.txt","w+")

guess_password = ''
i = int(0)

while guess_password != 'quit':
    pw_hash_tuple = hash_password("123456")
    guess_password = input('Enter password guess: ')
    if guess_password == 'quit':
        print('Thank you for guessing')
        hashtext.close() 
        sys.exit()
    validate = validate_password(guess_password, pw_hash_tuple)
    print (validate) # Truequit
    hashtext.write("This is guess %d: %s and is %s\n" %(i+1,guess_password, validate))
    i = i + 1
    