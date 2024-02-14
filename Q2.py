# Question 2: Fibonacci Sequence

# Write a program to generate the Fibonacci sequence up to 100.

# a fibonnaci sequence is the integer sentence where the first two terms are 0 and 1
# the next term will be the sum of the pevious two terms

num1=0 				#initialize num1 as 0
num2=1 				#initialize num2 as 1
next_term = None 	#create an empty variable to hold value of th next term
my_limit=100 		#set limit of series to 100

print('The Fibonacci Series: ')
#define a while loop that stops when the declared limit is reached
while (num1 <= my_limit):
	print(f'{num1}') 			#prints the first term of the series
	next_term = num1 + num2 	#place the sum of num1 and num2 into the empty variable next_term
	num1=num2 					#re-initialize value of num2 into num1
	num2=next_term   			#re-initialize value of next_term into num2
