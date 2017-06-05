print ("Time to play a guessing game.")

# ask computer to generate a random number
from random import * 
x = randint(1, 100)
print ("the computer takes " + str(x))

# Initialize ask for user to enter a number
y = int(raw_input("Enter a number between 1 and 100: "))
count = 1

# compare computer # vs. user #
while y != x: 
	print ("Too high") if y > x else "Too low"
	
	
	y = int(raw_input("Try again: "))
	count += 1
	

else:
	print ("Congratulations! You got it in " + str(count) + " guesses.")

	