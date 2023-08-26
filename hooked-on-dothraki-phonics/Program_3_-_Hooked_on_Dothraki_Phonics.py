##CS 101
##Program 1
##Christina Gerstner
##clgdtf@mail.umkc.edu
##
##Problem: Dothraki is a fantasy language used the Dothraki people in Game of Thrones.
##         Write a program to enter a dothraki word and output the International Phonetic
##         Alphabet pronunciation.
##              Ex - zhavvorsa is pronounced ʒavvoɾ, rsa.
##         IPA uses some special symbols. Ordinal value is given. You
##         should be able to cut-n-paste the characters into your program as well.
##              ● The program should validate that the word given by the user only has
##                valid Dothraki characters. Multiple words can be separated by a space.
##              ● If a word is not valid, warn the user about offending characters and
##                prompt for a hawaiian word again.
##              ● Ask the user if they want to do another word. Valid responses are
##                Y, YES, N or NO. If they want to play more, then they can enter another
##                Dothraki word. If no, then the program ends.

##
##ALGORITHM:
##      1. ask user for pronunciation.
##      2. validate whether or not user input has valid characters for translation
##      3. for loop that checks each char and adds correct ordinal value prununciation to an
##         empty string
##      4. print out tranlated pronunciation
##      5. ask user if they want to enter another word
##
##ERROR HANDLING: None
##
##OTHER COMMENTS: None
##################################################################################################
def splitWords(words):     # <- returns list of each word from user input if more than one word
	return words.split(' ')

def validateWord(word):     # <- string
	valid = True
	if word.strip() == '':
		return False
	newWord = word.lower().strip()
	for i in range(0, len(newWord)):
		currentChar = newWord[i]
		if i+1 < len(newWord):
			nextChar = newWord[i+1]
		else:
			nextChar = ' '

		if currentChar == 'c' and nextChar == 'h':
			valid = True
		elif currentChar in 'adefghijklmnoqrstvwyz':
			valid = True
		else:
			valid = False    # userInput is invalid
			
		if valid == False:
			return False     # b/c userInput is invalid, false is returned
	return True

# Legal characters -
# adefghijklmnoqrstvwyz
# ch,qa,qe,qi,qo,sh,kh,th,zh,h[-1]

def translateWord(word):
	tempTranslate = ''
	newWord = word.lower().strip()

	skip = False
	for i in range(0, len(newWord)):
		if skip == True:
			skip = False
			continue
		
		if i == len(newWord)-1 and newWord[i] == 'h':
			tempTranslate += chr(295)
		elif newWord[i] == 'h':
			tempTranslate += chr(104)
		elif newWord[i] == 'a':
			if newWord[i-1] == 'q':
				tempTranslate += chr(593)
			else:
				tempTranslate += chr(97)
		elif newWord[i] == 'e':
			if newWord[i-1] == 'q':
				tempTranslate += chr(603)
			else:
				tempTranslate += chr(101)
		elif newWord[i] == 'i':
			if newWord[i-1] == 'q':
				tempTranslate += chr(101)
			else:
				tempTranslate += chr(105)
		elif newWord[i] == 'o':
			if newWord[i-1] == 'q':
				tempTranslate += chr(596)
			else:
				tempTranslate += chr(111)
		elif newWord[i] == 'c':
			tempTranslate += (chr(116) + chr(865) + chr(643))
			skip = True
		elif newWord[i] == 's':
			if len(newWord) > i + 1 and newWord[i+1] == 'h':
				tempTranslate += chr(643)
				skip = True
			else:
				tempTranslate += chr(115)
		elif newWord[i] == 'k':
			if len(newWord) > i + 1 and newWord[i+1] == 'h':
				tempTranslate += chr(120)
				skip = True
			else:
				tempTranslate += chr(107)
		elif newWord[i] == 't':
			if len(newWord) > i + 1 and newWord[i+1] == 'h':
				tempTranslate += chr(952)
				skip = True
			else:
				tempTranslate += (chr(116) + chr(810))
		elif newWord[i] == 'z':
			if len(newWord) > i + 1 and newWord[i+1] == 'h':
				tempTranslate += chr(658)
				skip = True
			else:
				tempTranslate += chr(122)
		elif newWord[i] == 'd':
			tempTranslate += (chr(100) + chr(810))
		elif newWord[i] == 'f':
			tempTranslate += chr(102)
		elif newWord[i] == 'g':
			tempTranslate += chr(103)
		elif newWord[i] == 'j':
			tempTranslate += (chr(100) + chr(865) + chr(658))
		elif newWord[i] == 'l':
			tempTranslate += (chr(108) + chr(810))
		elif newWord[i] == 'm':
			tempTranslate += chr(109)
		elif newWord[i] == 'n':
			tempTranslate += (chr(110) + chr(810))
		elif newWord[i] == 'q':
			tempTranslate += chr(113)
		elif newWord[i] == 'r':
			tempTranslate += (chr(638) + chr(44) + chr(32) + chr(114))
		elif newWord[i] == 'v':
			tempTranslate += chr(118)
		elif newWord[i] == 'w':
			tempTranslate += chr(119)
		elif newWord[i] == 'y':
			tempTranslate += chr(106)

	return tempTranslate

def redoPronun(answer):
	while (answer != 'y') and (answer != 'n') and (answer != 'yes') and (answer != 'no'):
		print('You must enter only Y/YES/N/NO')
		answer = input('\nDo you want to try another word? Enter Y/YES/N/NO ==>\t').lower()
	if answer == 'yes' or answer == 'y':
		return True
	else:
		return False


repeat = True
while repeat == True:
	finalTranslation = ''
	userPronun = input('\nEnter a word to get the Dothroki pronunciation ==>\t')
	tempWordList = splitWords(userPronun)
	for w in tempWordList:
		if w == '':
			continue
		if len(finalTranslation) > 0:
			finalTranslation += ' '
		valid = validateWord(w)
		if valid != True:
			print('The word you entered had invalid characters. Please try again.')
			break
		else:
			#translateWord
			translatedPronun = translateWord(w)
			finalTranslation += translatedPronun

	if valid == True:
		print(userPronun.strip(), 'is pronounced', finalTranslation)

		#ask if user wants another pronunciation
		redo = input('\nDo you want to try another word? Enter Y/YES/N/NO ==>\t').lower()
		repeat = redoPronun(redo)
		


