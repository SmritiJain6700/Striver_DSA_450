'''Rotate Array By One
Last Updated : 23 Jul, 2025
Given an array, the task is to cyclically right-rotate the array by one. 

Examples:  

Input: arr[] = [1, 2, 3, 4, 5] 
Output: [5, 1, 2, 3, 4]

Input: arr[] = [2, 3, 4, 5, 1]
Output: [1, 2, 3, 4, 5]'''

def rotateArrayToRightByOneByShiftingElemets(arr):
    n = len(arr)
    # storing the last elemet
    ele = arr[-1]

    # shifting all the elements to the right by 1
    for i in range(n-2,-1,-1):
        arr[i+1] = arr[i]

    arr[0] = ele

    return arr

def rotateArrayToRightByOneByReversing(arr):
    # logic
    # in order to rotate the array by one
    # first reverse the first (n-1) elements of the array
    # then reverse the entire array
    # e.g [1,2,3,4,5] n = 5
    # first reverse the first 4 elements -- [4,3,2,1,5]
    # reverse the entire array -- [5,1,2,3,4]

    n = len(arr)
    # reverse the first (n-1) elements
    i = 0
    j = n-2
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
    
    return arr

arr = list(map(int, input("Enter the input: ").split(",")))
print(f"Rotated Array {arr} to right by one: ", rotateArrayToRightByOneByShiftingElemets(arr))
arr1 = list(map(int, input("Enter the input: ").split(",")))
print(f"Rotated Array {arr1} to right by one: ", rotateArrayToRightByOneByReversing(arr1))

