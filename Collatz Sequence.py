#  Max Gresoro - IT075 Sierra College
#  Chap 4 assingment to write a function that prints
#  the Collatz Sequence for a given user input

# define a function with a single variable passed
def collatz(number):

    if number % 2 == 0:  # check to see if the number is evenly divisable by 2
        return number // 2 # result is: number / 2

    elif number % 2 == 1:  # if not evenly divisable then calculate
        return 3 * number + 1  # result is: 3 * number + 1

#  main program starts here
number = 0
print('This program will print the Collatz Sequence for a number that you input')
print()
number = int(input('Kindly enter a whole number: '))
print()
print('The Collatz Sequence for',number,'is:')
collatz(number)
# create a loop to execute the collatz function until the resulting calculation is 1 and then stop
while number != 1:
    number = collatz(int(number))
    print(number)
