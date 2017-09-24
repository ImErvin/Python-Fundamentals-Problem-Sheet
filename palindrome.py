# Palindrome written by Ervin Mamutov - github.com/imervin

# function palindromeCheck takes in a string parameter
def palindromeCheck(someString):
    # Local variable nonReversedString is a list of characters that make up the string "someString"
    nonReversedString = [i for i in someString]
    # Local variable reversedString is a list of characters that make up the string "someString"
    # but looped over backwards. Adapted from https://stackoverflow.com/questions/869885/loop-backwards-using-indices-in-python
    reversedString = [someString[i] for i in range(len(nonReversedString)-1, -1, -1)]
    # If the two lists above equal, then it's a palindrome
    if(nonReversedString == reversedString):km
        print(someString,"is a palindrome!")
    # Or else it's not a palindrome
    else:
        print(someString,"is not a palindrome!")

# Ask the user for an input and pass that input into the function to check if it's a palindrome
palindrome = input("Type in a word to check if it's a palindrome: ")
palindromeCheck(palindrome)
