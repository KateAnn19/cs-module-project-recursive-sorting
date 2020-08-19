import math
# TO-DO: Implement a recursive implementation of binary search
    # Your code here
    # Returns index of x in arr if present, else -1 
def binary_search(arr, x, low, high): 
  
    # Check base case 
    if high >= low: 
  
        mid = math.floor((high + low)/2)
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, x, low, mid - 1) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, x, mid + 1, high) 
  
    else: 
        # Element is not present in the array 
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
#
def agnostic_binary_search(arr, key):
    # Your code here
     # Check base case 
    end = len(arr) - 1
    start = 0
    isAscending = False

    if arr[start] < arr[end]:
        isAscending = True
        
    while start <= end:
      #calculate the middle of the current range
        mid = math.floor(start + (end - start) / 2)

        if(key == arr[mid]):
            return mid

        if(isAscending): #ascending order
            if (key < arr[mid]):
                end = mid - 1 #the 'key' can be in the first half
            else: #key > arr[mid]
                start = mid + 1 #the 'key' can be in the second half
        else: #descending order        
            if (key > arr[mid]):
                end = mid - 1 #the 'key' can be in the first half
            else:#key < arr[mid]
                start = mid + 1 #the 'key' can be in the second half
        
    return -1 #element not found
    

