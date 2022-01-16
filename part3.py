"""
******
PART 3
******

Write a program that prompts the user to enter two integers, one representing the base of a rectangle, and one representing the height. The program will then print a rectangle made of asterisks (*) with those dimensions. 

(Hint: this may involve nested for loops(ie. a for loop inside a for loop), but it does not have to. Concatenating/adding strings ('*' + '*') or replicating strings ('*' * 3) may be helpful here.)

An example of what should appear on the console when the program runs:

Enter the base: 7
Enter the height: 3

*******
*******
*******

"""

b = int(input("Enter a base value: "))
h = int(input("Enter a height value: "))

for i in range (1, h + 1):
  for i2 in range (1, b + 1):
    print('*', end = " ")
  print( )
