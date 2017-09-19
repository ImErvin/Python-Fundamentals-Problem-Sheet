for i in range(100): # Using pythons range() function to create a list of numbers [0..99] so we can loop over it using a for statement
    if i % 3 == 0 and i % 5 == 0:   # If the index is a multiple 3 and the index is a multiple of 5, then print out "fizzbuzz"
        print("fizzbuzz")
    elif i % 3 == 0:    # If the index isn't a multiple of both 3 and 5, then check if it's only a multiple of 3
        print("fizz")   # If it is a multiple of 3, print "fizz"
    elif i % 5 == 0:    # If the index isn't a multiple of both 3 and 5 and it's not a multiple of 3, check if it's a multple of 5
        print("buzz")   # If it is a multiple of 5, print "buzz"
    else:   # If the index is not a multiple or 3 and 5 or 3 or 5, then just print out the index.
        print(i)