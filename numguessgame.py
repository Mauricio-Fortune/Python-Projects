# Mauricio Fortune
# COP 2930
# New Guess Game
# 10/3/2020


import random

#Get a random integer
correctnum= random.randint(1,100)

#Set the values of the amount of guesses to zero
numguesses = 0

#Set the amount of high guesses to zero
highguesses = 0

#Find the first guess
guess = int(input("What is your guess?\n"))

#Only run if the guess does not equal the correct number and if the high guesses are less than or equal to three
while guess != correctnum and highguesses <= 3:

    #If the guess is greater than the correct number
    if guess > correctnum:

        #Add one to the number of guesses
        numguesses = numguesses + 1

        #Add one to the number of high guesses
        highguesses = highguesses + 1

        #If the high guesses are less than or equal to zero
        if highguesses <= 3:
            
            #Print statement telling them their guess is too high
            print("Your guess is too high. You have made", highguesses," guesses that were too high.")

            #Find their next guess
            guess = int(input("What is your guess?\n"))

        #If the high guesses are greater than 3, print the losing statement
        else:
            print("Sorry you lost by making too many high guesses.\nThe correct number was ", correctnum,".", sep="")

    #If the guess is less than the correct number
    else:
        
        #Add one to the amount of guesses
        numguesses = numguesses + 1
        
        #Print statement telling them their guess was too low
        print("Your guess is too low.")

        #Find the next guess
        guess = int(input("What is your guess?\n"))

#If the correct number is guesses
if guess == correctnum:
    
    #Add one to the amount of guesses
    numguesses = numguesses + 1
    
    #Print the winning print statement
    print("Congrats, you got the number in",numguesses,"guesses, of which", highguesses,"were too high.")

