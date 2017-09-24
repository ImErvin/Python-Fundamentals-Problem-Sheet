import math

x = 10
z = 1
prevZ = 0

z_next = lambda z: z - ((z*z - x) / (2 * z))

while z != prevZ:
    print(z , "\n" ,prevZ)
    prevZ = z
    z = z_next(z)
    if(math.sqrt( x ) == z):
        print("true")
        break

print("Our guess: \t%.9f\nSqrt() method: \t%.9f" % (z, math.sqrt( x )))