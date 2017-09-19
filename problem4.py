# Function factorialSum takes parameter n
def factorialSum(n):
    # myList is a list with values between the parameter n and 0.
    # I use range with 3 parameters, (the start, end and increment value) (in this case I decrement by -1)
    # This results in [n,n-1....1]
    myList = [i for i in range(n, 0, -1)]
    print("\n",myList)

    # Using myList I can loop over each index and multiply it with the one after it. I create myListMultiplied
    # and set it to 1, because n*1 = n
    myListMultiplied = 1
    # I loop over myList and at every index I set the value of myListMultiplied to myListMultiplied * the current index
    # Which mimics what a factorial does.
    for n in myList:
        myListMultiplied = myListMultiplied * n
    print("\n",myListMultiplied)

    # Once I have the factorial of n, I can turn this integer into an array of numbers for example: 100 = [1,0,0]
    # I do this by looping over a stringifed version of myListMultiplied and turning each index into an array of ints
    mySumList = [int(x) for x in str(myListMultiplied)]
    print("\n",mySumList)

    # Once I have mySumList, I can loop over the list and add each index
    # I create mySumEvaluated and set it to int 0
    mySumEvaluated = 0
    # Loop over every index of mySumList and add it onto mySumEvaluated
    for j in mySumList:
        mySumEvaluated = mySumEvaluated + j
    # I use print() to print the value
    print("\nSum of factorial for 100! is: ",mySumEvaluated)

        
# Call the function and pass in the value 100
factorialSum(100)