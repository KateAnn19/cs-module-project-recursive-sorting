import math

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr1, arr2):
    #elements = len(arrA) + len(arrB)
    #merged_arr = [0] * elements
    #*********************************
    results = []
    #create pointers
    arr1Indx = 0;
    arr2Indx = 0;

    while arr1Indx < len(arr1) and arr2Indx < len(arr2):
        if(arr2[arr2Indx] > arr1[arr1Indx]):
            results.append(arr1[arr1Indx])
            arr1Indx += 1
        else:
            results.append(arr2[arr2Indx])
            arr2Indx += 1
    while(arr1Indx < len(arr1)):
        results.append(arr1[arr1Indx])
        arr1Indx += 1

    while(arr2Indx < len(arr2)):
        results.append(arr2[arr2Indx])
        arr2Indx += 1
    
    return results

print(merge([1,10,50], [2,14,99,100]))

#     #while there are still values we haven't looked at
#         #if the value in the first array is smaller than the value in the second array, push the value in the first array
#         #into out results and move on to the next value in the first array
#         #if the value in the first array is larger than the value in the second array, push the value in the second array into
#         #our results and move on to the next value in the second array
#         #once we exhaust one array, push in all remaining values from the other array
#         #sort values all in the same way
    

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if(len(arr) <= 1):
        return arr
    mid = math.floor(len(arr)/2)
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:len(arr)])
    return merge(left, right)

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

    

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

