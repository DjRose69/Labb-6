
def binarySearch(mylist, target):
    # class for binary search
    first = 0 
    last = len(mylist)-1
    counter = 0
    found = False # initializing to False

    while found == False:
        
        counter += 1
        mid = (first + last)//2 # middle index is equal to first plus last index divided by 2

        if mylist[mid] == target:
            # while loop is broken, target found
            found = True

        elif len(mylist) == 0:
            # the targeted element is not in list
            break

        else:
            if target < mylist[mid]:
                '''
                if target is less than the element at middle index,
                we need to search on the halve of the list that is
                LESSER than the current middle - hence we define
                our new last as mid MINUS 1'''
                last = mid - 1
            else:
                '''
                opposite is true of target is GREATER than the element
                at middle index, we need to search on the right halve 
                of our list, hence first is mid PLUS 1'''
                first = mid + 1




