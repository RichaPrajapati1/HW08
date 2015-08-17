##############################################################################
################################ IMPORTS: ####################################
##############################################################################
import sys
import random


##############################################################################
############################## FUNCTIONS: ####################################
##############################################################################
def game(NumberOfDigits):
	"""This function takes in the number of digits and generates a random 
	number confirming to the specified number of digits. It then asks the user 
	to guess the random number while providing basic feedback to the user 
	depending on his/her guesses. The funtion terminates once the user has 
	guessed the numner correctly
	"""
	MinNum = 10**(NumberOfDigits - 1) 	#Finding the minimum possible number given the number of digits
	MaxNum = (10**NumberOfDigits) - 1 	#Finding the minimum possible number given the number of digits
	Num = random.randint(MinNum,MaxNum) 	#Generating a random number of the specified number of digits
	NumberOfTries = 0

	print ("Let's play the mimsmind0 game.")

	GuessStr = raw_input("Guess a {0}-digit number: " .format(NumberOfDigits))
	while True:							#This loop with keep asking the user to guess the number till he/she guesses the correct number
		NumberOfTries += 1
		try:							#Validating whether the given input is a valid integer
			GuessNum = int(GuessStr)
		except:
			GuessStr = raw_input("Invalid input. Try again: ")
			continue
		else:
			if len(GuessStr) != NumberOfDigits:		##Validating whether the given input contains the specified number of digits
				GuessStr = raw_input("Invalid input. Try again: ")
				continue
			else:
				if GuessNum == Num:
					print ("Congratulations. You guessed the correct number in {0} tries" .format(NumberOfTries))
					break				#Getting out of the loop on correct guess
				elif GuessNum < Num:
					GuessStr = raw_input("Try again. Guess a higher number: ")
					continue			
				else:
					GuessStr = raw_input("Try again. Guess a lower number: ")
					continue

##############################################################################
################################ MAIN: #######################################
##############################################################################
def main():
	try:
		NumberOfDigits = int(sys.argv[1])
	except:
		NumberOfDigits = 3
	game(NumberOfDigits)



if __name__ == '__main__':
    main()
