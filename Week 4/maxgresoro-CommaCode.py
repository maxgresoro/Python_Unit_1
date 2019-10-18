#  Max Gresoro - IT075 Sierra College
#  Assingment to Write a function that takes a
#  list value as an argument and returns a string
#  with all the items separated by a comma and a space,
#  with and inserted before the last item

spam = ['apples', 'bananas', 'tofu', 'cats']

# define function to convert list to string
def CommaCode(ListIn):
    ListString = ''  # initialize string variable
    for i in range(len(ListIn[:-1])):
        ListString = ListString + str(ListIn[i]) + ', '  # build string of a list
    ListString = ListString + 'and ' + str(ListIn[-1])  # insert and before last item
    return (ListString)  # return the string

# begin main program here
print('This program will convert a list to a string with seperators')
print()
print('The original list is:', spam)
print()
print('The converted list is:', CommaCode(spam)) # call function to convert list to string

