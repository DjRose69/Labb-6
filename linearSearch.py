
def linearSearch(mylist, target):
    # class for linear search
    counter = 0
    for index in range(len(mylist)):
        # systematically goes through every element in list

        counter += 1
        if mylist[index] == target:

            # if the specific element is equal to the target return True
            return True
    # otherwise return False
    return False



