# Question 6: Count Vowels

# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2


print('Below is a program that takes a sentence of word as input and return the number of vowels it contains.')
snippet = str(input('Input your senstence/word here: ')) 	#initialize a string variable

my_vowels= ['a','e','i','o','u'] 	#declare a list containing all the vowels
count = 0 							#initialize count to begin at 0

# begin a for loop to iterate over the snippet variable
for i in range(len(snippet)):
	if snippet[i] in my_vowels: 	#use in operator to determine whether vowel values are in the snippet sequence
		count+=1 					#if vowel found increment the value of count

print(f'Your sentence has {count} vowels')  	#print out the number of vowels found
	
	



