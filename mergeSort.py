
'''
Merge-Sort is a Divide and Conquer Algorithm. We divide the
initial array into two parts, Left and Right, divided from the middle. 
We then recursively call the same function, and keep dividing the
left and right arrays by their middle point until we only have 
one element in each array. Then the merging process is activated,
and we merge all the single elements into one, sorted array.
'''

def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements into 2 halves:
        left = arr[:mid] # left halve
        right = arr[mid:] # right halve
        


        # Sorting the first half
        mergeSort(left)
        # Sorting the second half
        mergeSort(right)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left halve is used
                arr[k] = left[i]
                # move the iterator forward
                i += 1
            else:
                # the vaue from the right halve is used
                arr[k] = right[j]
                j += 1

            # move to next slot
            k += 1
  
        # Checking if any remaining values
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
  

