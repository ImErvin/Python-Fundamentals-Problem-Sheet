# Guessing game written by Ervin Mamutov - github.com/imervin

# Import random to create a random number
import random

secretNumber = random.randint(0,1000) # The secret number is generated randomly every game
noOfTries = 0 # Number of attempts
prevGuess = 0 # A temp variable to store the previous guess

# Function makeGuess takes parameter n
def makeGuess(currentGuess):
    # Reference the global variables
    global noOfTries 
    global prevGuess

    # If it's the first attempt
    if(noOfTries == 0):
        # I set the previous guess to the current guess
        prevGuess = currentGuess
        # And I increment the number of attempts
        noOfTries = noOfTries + 1
    
    # If the previous guess is not equal the current guess
    if(prevGuess != currentGuess):
        # I increment the number of attempts
        noOfTries = noOfTries + 1

    # Set the previous guess to the current guess for condition above
    prevGuess = currentGuess

    # If the current guess is equal to the secretNumber then you win
    if(currentGuess == secretNumber):
        print("Congratulations! You win.\n")
        # Print out the number of attempts minus 1 because the the winning attempt does not count
        print("It only took you", noOfTries - 1, "tries to solve this puzzle")

    # Else if the current guess is less than the secretNumber, notify the player and use recursion to guess again
    elif(currentGuess < secretNumber):
        print("Your guess is less than the secret number! Try again.")
        guess = input("What's your guess: ")
        makeGuess(int(guess))

    # Else if the current guess is greater than the secretNumber, notify the player and use recursion to guess again
    elif(currentGuess > secretNumber):
        print("Your guess is greater than the secret number! Try again.")
        guess = input("What's your guess: ")
        makeGuess(int(guess))

    # This shouldn't be activated, if it is, then there was some sort of error in the code.
    else:
        print("error")

# Welcome message
print("-------------------------\nWelcome to the guessing game\nThe secret number is randomly generated between 0-1000!\n-------------------------\n")

# Infinite loop to prompt the player for a guess
while True:
    # Using a try/catch to ensure the number entered is of numeric value
    try:
        guess = input("What's your guess: ")
        # Turn the input into an int and pass it into makeGuess function
        makeGuess(int(guess))
        # Exit condition out of the infinite loop
        break
    except ValueError:
        # Error message
        print ("Please enter a numeric value.")




