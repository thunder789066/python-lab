##CS 101
##Program 1
##Christina Gerstner
##clgdtf@mail.umkc.edu
##
##Problem: Samuel Pepys sent a letter to Isaac Newton concerning probabilities of dice. He had made a
##  wager and wanted to know the probabilities concerning the wager. In short given a 6 sided die,
##  he wanted to know which of the following had the greater chance of occuring.
##      1. At least one 6 occurs when six dice are rolled
##      2. At least two sixes occur when 12 dice are rolled
##      3. At least three sixes occur when 18 dice are rolled.
##  While this problem is trivial to solve with probabilities, we want to write a program to simulate
##  doing this many time over.

##
##ALGORITHM:
##      1. Display dice facts, ask for user input for # of trials
##      2. for loop that counts each trials given from user input, 3 separate for loops that count the
##         roll --> range(1,6)-> count 1 6 & range(1,12)-> count 2 6's & range(1,18)-> count 3 6's
##      3. Once all trials are done --> calculate final percentage results & display them
##      4. ask for user input to play again
##
##ERROR HANDLING: None
##
##OTHER COMMENTS: None
#####################################################################################################
import random

print('Die Odds')
print('Samuel Pepys once asked Isaac Newton which is more likely')
print('* At least 1 six occur when 6 dice are rolled')
print('* At least 2 sixes occur when 12 dice are rolled')
print('* At least 3 sixes occur when 18 dice are rolled')

play = True
while(play):
    print('\nEnter the number of trials to throw the dice\n')

    num_of_trials = int(input('How many trials? ==>\t'))
    while num_of_trials < 10:
        print('The number of trials must be 10 or larger\n')
        num_of_trials = int(input('How many trials? ==>\t'))

    success_1_to_6 = 0
    success_1_to_12 = 0
    success_1_to_18 = 0

    for trial in range(num_of_trials):

        for i in range(1, 7):
            found_1_to_6 = 0
            roll1 = random.randint(1,6)
            if roll1 == 6:
                found_1_to_6 += 1
            if found_1_to_6 >= 1:
                success_1_to_6 += 1
                break
            
        found_1_to_12 = 0
        for i in range(1, 13):
            roll2 = random.randint(1,6)
            if roll2 == 6:
                found_1_to_12 += 1
            if found_1_to_12 >= 2:
                success_1_to_12 += 1
                break

        found_1_to_18 = 0
        for i in range(1, 19):
            roll3 = random.randint(1,6)
            if roll3 == 6:
                found_1_to_18 += 1
            if found_1_to_18 >= 3:
                success_1_to_18 += 1
                break

    # ans -> answer for 1 to 6, 1 to 12, or 1 to 18
    # this converts answer to percentage
    ans6 = (float(success_1_to_6)/float(num_of_trials)) * 100
    ans12 = (float(success_1_to_12)/float(num_of_trials)) * 100
    ans18 = (float(success_1_to_18)/float(num_of_trials)) * 100

    print('\nAt least one die was a six when 6 are rolled', ans6, '%')
    print('At least two die was a six when 12 are rolled', ans12, '%')
    print('At least three die was a six when 18 are rolled', ans18, '%')

    # if statement criteria
    if ans6 > ans12 and ans6 > ans18:
        print('\nAt least one die was a six when 6 are rolled occurred the most.')
    elif ans12 > ans6 and ans12 > ans18:
        print('\nAt least two die was a six when 12 are rolled occurred the most.')
    elif ans18 > ans6 and ans18 > ans12:
        print('\nAt least three die was a six when 18 are rolled occurred the most.')
    elif ans6 == ans12 and ans6 == ans18:
        print('\nIn this run they are all 3 likely. Try it with more trials')
    elif ans6 == ans12:
        print('\nAt least one die was a six when 6 are rolled and')
        print('At least two die was a six when 12 are rolled occurred the most.')
        print('Try again with more trials.')
    elif ans6 == ans18:
        print('\nAt least one die was a six when 6 are rolled and')
        print('At least three dice were a six when 18 are rolled occurred the most.')
        print('Try again with more trials.')
    elif ans12 == ans18:
        print('\nAt least two die was a six when 12 are rolled and')
        print('At least three dice were a six when 18 are rolled occurred the most.')
        print('Try again with more trials.')

    # asks user if they want to play again
    replay = input('\nDo you want to play again? Y/YES/N/NO ==>\t')
    replay = replay.lower()
    while (replay != 'y') and (replay != 'n') and (replay != 'yes') and (replay != 'no'):
        print('You must enter Y YES or N NO\n')
        replay = input('Do you want to play again? Y/YES/N/NO ==>\t')
        replay = replay.lower()

    if replay == 'y' or replay == 'yes':
        play = True
    else:
        play = False

