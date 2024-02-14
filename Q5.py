# Question 5: Reverse Integer

# Write a program that takes an integer as input and returns an integer 
# with reversed digit ordering.

# Examples:
# For input 500, the program should return 5.
# For input -56, the program should return -65.
# For input -90, the program should return -9.
# For input 91, the program should return 19.

#initialize your variable to contain the inputed integer
my_int = int(input('Input your number here: '))

# begin an if statement to check whether inputed value is of int type
if (type(my_int) == int):
	reversed_str = str(my_int)[::-1]
	print(reversed_str)

# if not an integer type, return an error message
elif (type(my_int) != int):
	print('Inputed value is not of integer type')
	
# if no value was inputted, return an error
else:
	print('Kindly input a value')





