# function palindromeCheck takes in a string parameter
def palindromeCheck(someString):
    # Local variable nonReversedString is a list of characters that make up the string "someString"
    nonReversedString = [i for i in someString]
    # Local variable reversedString is a list of characters that make up the string "someString"  
    reversedString = [someString[i] for i in range(len(nonReversedString)-1, -1, -1)]
    if(nonReversedString == reversedString):
        print(someString,"is a palindrome!")
    else:
        print(someString,"is not a palindrome!")

palindrome = input("Type in a word to check if it's a palindrome: ")
palindromeCheck(palindrome)