# list sort written by Ervin Mamutov - github.com/imervin

import random

# mergeList function takes 2 lists as parameters
def mergeLists(list1, list2):
    # Sorts the two lists
    list1.sort()
    list2.sort()

    #Print out the two lists that have been passed in
    print("List One:",list1,"\nList Two:",list2)
    
    # Concats the two lists above to create a new list
    list3 = list1+list2

    # Sorts the new list
    list3.sort()

    # Prints the new list
    print(list3)

# Pass in two random lists into the function above
mergeLists([random.randint(1, 100) for i in range(10)], [random.randint(1, 100) for i in range(10)] )
