'''https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
There may be duplicates in the original array.
Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.'''

# Logic:
# if an array is sorted in non-decreasing order then the previous element is always smaller or euqal to the current element  
# So, if we rotate it by some point (Clockwise or Anticlockwise) , there exists a diversion where the previous element is greater 
# or equal to the current element. If there is at most one diversion then we can say that the array is sorted and rotated.

# time-complexity - O(n) -- as we are traversing over the array
# space-complexity - O(1) 

def checkIfArrayIsSortedAndRotated(arr):
    n = len(arr)
    # no of diversions
    diversions = 0

    for i in range(1, n):
        if(arr[i-1] <= arr[i]):
            continue
        else:
            diversions += 1

    if(arr[n-1] > arr[0]):
        diversions += 1

    if(diversions <= 1):
        return True
    else:
        return False
    
arr = list(map(int, input("Enter the input: ").split(",")))
x = checkIfArrayIsSortedAndRotated(arr)
if(x):
    print(f"The array {arr} is sorted and rotated.")
else:
    print(f"The array {arr} is not sorted.")
    



