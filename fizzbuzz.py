# Fizzbuzz written by Ervin Mamutov - github.com/imervin

# Using pythons range() function to create a list of numbers [0..99] so we can loop over it using a for statement
for i in range(100):
    # If the index is a multiple 3 and the index is a multiple of 5, then print out "fizzbuzz"
    if i % 3 == 0 and i % 5 == 0:   
        print("fizzbuzz")
    # If the index isn't a multiple of both 3 and 5, then check if it's only a multiple of 3
    elif i % 3 == 0:
        # If it is a multiple of 3, print "fizz"
        print("fizz")
     # If the index isn't a multiple of both 3 and 5 and it's not a multiple of 3, check if it's a multple of 5
    elif i % 5 == 0: 
        # If it is a multiple of 5, print "buzz" 
        print("buzz")
    # If the index is not a multiple or 3 and 5 or 3 or 5, then just print out the index.
    else:   
        print(i)