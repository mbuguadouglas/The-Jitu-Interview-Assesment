# Question 3: Power of Two

# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples:

# 8=> returns true
# 6=> returns false

# explin to the user what the program does and take their input
print('The below program takes an input integer and returns true if it is a power of 2, else it returns false...')
my_num= int(input('Input a number to work with here: '))

# check whether the number is divisible by 2
if (my_num%2 == 0):
	print('True')
# check whether the number is not divisible by 2
elif (my_num%2 != 0):
	print('False')
# what to do incase of wrong input
else:
	print('Please input a valid number!')







