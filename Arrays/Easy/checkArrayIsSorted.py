# Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.
# Examples:
# Input : nums = [1, 2, 3, 4, 5]
# Output : true
# Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

# time - complexity - O(n)
# space - complexity - O(1)
def checkIfArrayIsSorted(arr):
    n = len(arr)
    if(len(arr) == 1):
        return True
    
    for i in range(1,n):
        if(arr[i] >= arr[i-1]):
            continue
        else:
            return False
    
    return True

arr = [2,4,1,3]
print(f"Array {arr} is sorted: ", checkIfArrayIsSorted(arr))

arr1 = [12,56,78,99,100]
print(f"Array {arr1} is sorted: ", checkIfArrayIsSorted(arr1))