# Question 1: FizzBuzz

# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for
# multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print
# "FizzBuzz"

# initialize your variable 
i=1

# create the loop and set its range from 1 to 100
for i in range(1,101):
	#see whether the variable is a multiple of 3
	if (i%3==0):
		print(f'{i}: Fizz')
	# see whether the variable is a multiple of 5
	elif (i%5==0):
		print(f'{i}: Buzz')
	#see whether the variable is a multiple of both 3 AND 5
	elif (i%3==0) and (i%5==0):
		print(f'{i}: FizzBuzz')
	#check if variable is not a multple of both
	# else:
		# print(f'The value of i is: {i}, which is neither a multiple of 3 or 5')
	#increment the variable to move onto next digit
	i=i+1



