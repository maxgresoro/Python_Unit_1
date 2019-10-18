#  Max Gresoro - IT075 Sierra College
#  Assingment to calculate the number of trees within a city

print();
print("This program will calculate the number of trees in a city");
print();
print("We will use the method of estimating the number of trees in a city block");
print("by taking an average of 5 city blocks in different parts of the city");
print();
print("Use Google maps to count the number of trees in a city block");
print();
print("The program will then use that estimate multiply it by the total land area");
print("within the city limits");
print();
input("Press enter to continue");
print();
print();

#  the following inputs will be used to determine number of trees in a defined area
trees1 = float(input("How many trees in city block #1? : "));  #sample block 1
trees2 = float(input("How many trees in city block #2? : "));  #sample block 2
trees3 = float(input("How many trees in city block #3? : "));  #sample block 3
trees4 = float(input("How many trees in city block #4? : "));  #sample block 4
trees5 = float(input("How many trees in city block #5? : "));  #sample block 5
avgtrees = (trees1 + trees2 + trees3 + trees4 + trees5)/5;


# the following inputs will be used to determine land area
print();
block1 = float(input("How many feet is one side of a city block? : "));  #input block length
block2 = float(input("How many feet is the other side of a city block? : "));  #input block length
citysqmi = float(input("How many sqare miles of land is in the city? : "));  #input block length
print();

# the following calculation will average the number of trees for 5 sampled blocks
# that number will be multiplied by the number of blocks in the city
# the number of blocks in the city is calculated by taking the total square feet
# of the city area divided by the total square feet of a block
citysqft = citysqmi*5280*5280;  # convert square miles to square feet
cityblocks = block1*block2;  # calculate city block square feet
totaltrees = (avgtrees * citysqft / cityblocks); # calculate total trees

print();
print("There are and average of",round(avgtrees), "trees in each city block");
print("There are",round(cityblocks), "city blocks within the city limits");
# Output the result by rounding to the nearest whole number
print("There are approximately",round(totaltrees), "trees within the city limits");
