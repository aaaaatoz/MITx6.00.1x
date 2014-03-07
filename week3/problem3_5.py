# When your hangman function passes the checks in the previous
# box, paste your function definition here to test it on harder 
# input cases.

import string
def hangman(secretWord):
	###initialise the variables
	lettersGuessed = []
	mistakesMade = 0
	availableLetters = [ x for x in string.ascii_lowercase ]
	secretWord = secretWord.lower()
	print "Welcome to the game Hangman!"
	print "I am thinking of a word that is %d letters long" %len(secretWord)
	
	while mistakesMade < 8:
		print "-----------"
		print "You have %d guesses left" %(8-mistakesMade)
		print "Available Letters:" + "".join(availableLetters)
		currentLetter = raw_input("Please guess a letter: ")
		currentLetter = currentLetter.lower()
		if currentLetter in lettersGuessed:	    # already guessed
			print "Oops! You've already guessed that letter: "  + getGuessedWord(secretWord, lettersGuessed)
			continue
		else:
			availableLetters.remove(currentLetter)
			lettersGuessed.append(currentLetter)
			if currentLetter not in secretWord:		#get wrong guess
				mistakesMade += 1
				print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
			else:
				print "Good guess: "+ getGuessedWord(secretWord, lettersGuessed)
				if isWordGuessed(secretWord, lettersGuessed):
					print "------------"
					print "Congratulations, you won!"
					return
	print "-----------"
	print "Sorry, you ran out of guesses. The word was %s. " %secretWord
