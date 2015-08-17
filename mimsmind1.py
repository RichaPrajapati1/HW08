##############################################################################
################################ IMPORTS: ####################################
##############################################################################
import sys
import random
import string

##############################################################################
############################## FUNCTIONS: ####################################
##############################################################################
def game(NumberOfDigits):
	"""This function takes in the number of digits and generates a random 
	string confirming to the specified number of digits. It then asks the user 
	to guess the random number while providing basic feedback to the user 
	depending on his/her guesses. The funtion terminates once the user has 
	guessed the numner correctly or exhausted his trials
	"""
	Num_Str = ''.join(random.choice(string.digits) for _ in range(NumberOfDigits)) #Generating a random number of the specified number of digits
	# Num_Str = '007'
	NumberOfTries = 0
	MaxTries = (2**NumberOfDigits) + NumberOfDigits
	Bull = 0
	Cow = 0

	print ("Let's play the mimsmind1 game. You have {0} guesses." .format(MaxTries))

	GuessStr = raw_input("Guess a {0}-digit number: " .format(NumberOfDigits))
	NumberOfTries += 1
	while True:							#This loop with keep asking the user to guess the number till he/she guesses the correct number
		if NumberOfTries >= MaxTries:
			print ("Sorry. You did not guess the number in {0} tries. The correct number is {1}" .format(MaxTries, Num_Str))
			break
		try:							#Validating whether the given input is a valid integer
			GuessNum = int(GuessStr)
		except:
			GuessStr = raw_input("Invalid input. Try again: ")
			continue
		else:
			if len(GuessStr) != NumberOfDigits:		#Validating whether the given input contains the specified number of digits
				GuessStr = raw_input("Invalid input. Try again: ")
				continue
			elif GuessStr == Num_Str:
				print ("Congratulations. You guessed the correct number in {0} tries" .format(NumberOfTries))
				break
			else:
				Bull = 0
				Cow = 0
				for i in range(len(GuessStr)):		#This loop will count the number of bulls
					for j in range(len(Num_Str)):
						if GuessStr[i] == Num_Str[j] and i == j:
							Bull += 1
							break
				Temp_Num_Str = Num_Str 				#Making a temporary variable to store the random generated number for the next guess
				for letter in GuessStr:				#This loop will count the number of cows (including bulls)
					if letter in Temp_Num_Str:
						index = Temp_Num_Str.find(letter)
						Cow += 1
						Temp_Num_Str = Temp_Num_Str[:index] + Temp_Num_Str[index+1:]
						
				Cow = Cow - Bull					#Removing the double counts in cows
		GuessStr = raw_input("{0} bull(s), {1} cow(s). Try again: " .format(Bull,Cow))
		NumberOfTries += 1							#Incrementing the trial counter

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
