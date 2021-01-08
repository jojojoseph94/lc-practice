"""
Write a C function to return minimum and maximum in an array. Your program should make the minimum number of comparisons. 

Solution 1 : Do linear search and comparisons. There would be 2n comparisons in worst case.

Solution 2 : Compare in pairs, maximum if 3n/2 comparisons

** Why this question?
"""

# Python3 program of above implementation 
def getMinMax(arr):
    min_arr = arr[0]
    max_arr = arr[0]
    for i in range(len(arr)):
        if nums[i] < min_arr:
            min_arr = nums[i]
        elif nums[i] > max_arr:
            max_arr = nums[i]
    return (min_arr, max_arr)

def getMinMaxOptimized(arr):
    if len(arr)%2:
        min_arr = arr[0]
        max_arr = arr[0]
    else:
        min_arr = arr[0]
        max_arr = arr[1]
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i+1]:
            min_arr = min(min_arr, arr[i+1])
            max_arr = max(max_arr, arr[i])
        else:
            min_arr = min(min_arr, arr[i])
            max_arr = max(max_arr, arr[i+1])
    return (min_arr, max_arr)