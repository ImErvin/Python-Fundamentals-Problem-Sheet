# Smallest/largest written by Ervin Mamutov - github.com/imervin

# Import random to generate random lists
import random 

# Function smallestLargest takes a list as a parameter
def smallestLargest(someList):
    # I set the temp variables largest and smallest to the first index of the list
    # it will use these first values as a comparrison in the for loop
    largest = someList[0]
    smallest = someList[0]
    
    # Loops over the list
    for i in someList:
        # If the current value is greater than the largest value, set the current value as the largest
        if(i >= largest):
            largest = i
        # If the current value is smaller than the smallest value, set the current value as the smallest
        if(i <= smallest):
            smallest = i

    # Print out the results
    print("List recieved:\n",someList,"\n")
    print("Smallest:",smallest,"Largest=",largest)

# Create a list of 25 random numbers between 1 and 100
myList = [random.randint(1, 100) for i in range(25)]
# Pass the list into the the function
smallestLargest(myList)
