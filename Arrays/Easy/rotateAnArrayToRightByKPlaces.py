# https://leetcode.com/problems/rotate-array/description/
'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]'''

# time - complexity - O(n)
# space - complexity - O(n)
def rotateAnArrayToRightBykPlacesUsingExtraSpace(arr:list[int], k:int) -> None:
    n = len(arr)

    # now k can be greater than n so
    k = k%n

    if(k == 0):
        return 
    
    # create a temporary list to store the rotated elemets
    res = [0]*n

    for i in range(n):
        if(i < k):
            res[i] = arr[n-k+i]
        else:
            res[i] = arr[i-k]
    
    for i in range(0,n):
        arr[i] = res[i]

# time - complexity - O(n)
# space - complexity - O(1)
def rotateArrayToRightByKPlacesByReversingParts(arr:list[int], k:int) -> None:
    n = len(arr)

    k = k%n

    # first reverse the n-k elements of the array
    i = 0
    j = n-k-1
    while(j > i):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    # second reverse the last k elements of the array
    i = n-k
    j = n-1
    while(j > i):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    
    # now reverse the entire array
    i = 0
    j = n-1
    while(j > i):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    
arr = list(map(int, input("Enter the array to be rotated: ").split(",")))
k = int(input("Enter the no of places by which u want to rotate: "))
rotateAnArrayToRightBykPlacesUsingExtraSpace(arr,k)
print(F"Rotated array {arr} by {k} places", arr)

    
arr1 = list(map(int, input("Enter the array to be rotated: ").split(",")))
k = int(input("Enter the no of places by which u want to rotate: "))
rotateArrayToRightByKPlacesByReversingParts(arr1,k)
print(F"Rotated array {arr1} by {k} places Using Optimal Method", arr1)