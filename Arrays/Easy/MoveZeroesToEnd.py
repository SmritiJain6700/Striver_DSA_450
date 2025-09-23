# https://leetcode.com/problems/move-zeroes/description/
'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]'''

# Naive Approach
# time - complexity - O(n)
# space - complexity - O(n) -- temporary array used
def moveZeroesToEndUsigExtraSpace(arr):
    n = len(arr)
    # creating a temporary array to store the nonn-zero elements
    temp = list()

    for i in range(0, n):
        if(arr[i] != 0):
            temp.append(arr[i])

    # now update the elements in the final array
    j = len(temp)
    for i in range(0,n):
        if(i < j):
            arr[i] = temp[i]
        else:
            arr[i] = 0
    
# better Approach
# time - complexity - O(n)
# space - complexity - O(1)
def moveZeroesToEndInTwoTraversal(arr):
    n = len(arr)

    # in first traversal move the non-zero elements to the left
    ind = 0
    for i in range(0,n):
        if(arr[i] != 0):
            arr[ind] = arr[i]
            ind += 1
    # in second traversal make the remaining places as 0
    for j in range(ind, n):
        arr[j] = 0

# Optimal Approach
# time - complexity - O(n)
# space - complexity - O(1)
def moveZeroesTOEndInOneTraversal(arr):
    n = len(arr)

    ind = 0 #denotes index of the non-zero element

    for i in range(0,n):
        if(arr[i] != 0):
            arr[ind], arr[i] = arr[i], arr[ind]
            ind += 1

arr = list(map(int, input("Enter the array elements: ").split(",")))
moveZeroesToEndUsigExtraSpace(arr)
print("moveZeroesToEndUsigExtraSpace",arr)

arr1 = list(map(int, input("Enter the array elements: ").split(",")))
moveZeroesToEndInTwoTraversal(arr1)
print("moveZeroesToEndInTwoTraversal",arr1)

arr2 = list(map(int, input("Enter the array elements: ").split(",")))
moveZeroesTOEndInOneTraversal(arr2)
print("moveZeroesTOEndInOneTraversal",arr2)

