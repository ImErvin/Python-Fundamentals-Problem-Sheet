# Reverse string written by Ervin Mamutov - github.com/imervin

# Ask the user for an input, use that input to reverse and print it.
stringInput = input("Enter a string to reverse it: ")
# Adapted from https://stackoverflow.com/questions/931092/reverse-a-string-in-python
# stringInput[start,end,step], could specify [len(stringInput):0:-1] but works just as well by using [::-1]
print(stringInput[::-1])