
def bubbleSort(arr):
    '''
    Bubble sort goes through a list and compares elements next to each other. 
    If an element on the right is greater than one on the left, the elements are swapped. 
    This happens until the list is sorted.
    '''

    n = len(arr)
 
    # traversing through every element in array
    for i in range(n-1):
    # range(n) also work but outer loop will
    # repeat one time more than needed.
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                tmp1 = arr[j + 1]
                arr[j+1] = arr[j]
                arr[j] = tmp1
                

'''
Explanation: 
First, the outer for loop arrives at index zero.
The inner for-loop compares the element at index zero to the next 
element [0+1], if array[0] > array[1], they swap places.
The inner for loop will then KEEP comparing the element at array[0] to every 
element in array, to see if they need to swap places.
Then we start over at index 1 in the outer for-loop, 
and in the inner for-loop we check if array[1]>array[2], then
if array[1] > array[3] and so on up until index n - i - 1
This keeps going until the list is sorted and the outer for loop
has gone through all of the elements.
'''

