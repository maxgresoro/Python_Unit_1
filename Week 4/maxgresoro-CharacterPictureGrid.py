#  Max Gresoro - IT075 Sierra College
#  Chap 4 assingment to draw a character picture grid

grid = [['.', '.', '.', '.', '.', '.'],  # input the grid as a matrix
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print("The original picture grid looks like this")
for j in range(len(grid)): # setup the lenth of the grid in the x direction
    for i in range(len(grid[0])): # setup the length of the grid in the y direction
        print(grid[j][i],end='') # print grid going down the y direction first, end='' prevents a new line from printing
    print('')  # executes a new line after the i in range completes

print('')
print('')
print("By changing the loop structure the picture grid will pring like this")

for j in range(len(grid[0])): # setup the lenth of the grid in the x direction
    for i in range(len(grid)): # setup the length of the grid in the y direction
        print(grid[i][j],end='') # print grid going down the y direction first, end='' prevents a new line from printing
    print('')  # executes a new line after the i in range completes

print('')
print('')
print("Bye, bye...")
