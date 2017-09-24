# Newtons method for square roots written by Ervin Mamutov - github.com/imervin

# Import the math library to use the sqrt() function
import math

# X is the number that we want to find the square root of
x = 10.0
# Z is the initial variable passed into newton's formula
z = 1.0
# prevZ is the previous answer
prevZ = 0.0

# Using an anonymous function that takes an argument "z" I can pass in
# a new variable to get closer to the square root of a number.
z_next = lambda z: z - ((z*z - x) / (2 * z))

# While the current value of z is not the same as the previous value of z,
# the idea is that each time this loops, it will get closer to the square root.
# Sooner or later the formula will produce the same number and once that happens we
# know that the square root has been found.
while z != prevZ:
    # Print out z to see the algorithm in action.
    print(z)
    # Set the previous value of z to the current value
    prevZ = z
    # Use the lambda function to calculate a new value of z,
    # one that is closer to the square root of x.
    z = z_next(z)
    
    # After testing this out on a couple of numbers I found that certain numbers would get stuck
    # in the looping phase because the current and previous values of z would be almost identical
    # but after each iteration, one would have an extra decimal point. E.g: 
    # Current z:  3.162277660168379
    # Previous z: 3.1622776601683795
    # I used the the sqrt() function to catch it out.
    if(math.sqrt( x ) == z):
        break

# Print out the results.
print("---------------\nSquare root of %d\nOur guess: \t%.9f\nSqrt() method: \t%.9f" % (x, z, math.sqrt( x )))