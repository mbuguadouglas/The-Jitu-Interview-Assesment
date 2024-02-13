# Question 4: Capitalize Words

# Write a program that accepts a string as input, capitalizes the first letter of each word in the
# string, and then returns the result string.

# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

# Here we will emply the string method str.title().
# it returns a titlecased version of the string where words start with an uppercase 
# character and the remaining characters are lowercase.

# tell the user wha the program does
print('Below is a program that capitalizes each word in sentence..')
my_snippet = str(input('Kindly input your word/sentense here: '))

# initialize a function that takes in a string as it parameters
def capitalize(my_snippet):
	capitalized_snippet = my_snippet.title()  #declare a variable that contains the .title() method used on the inputed string
	return capitalized_snippet  			  #and returns its capitalization

print(capitalize(my_snippet)) 				#print the output to the terminal



