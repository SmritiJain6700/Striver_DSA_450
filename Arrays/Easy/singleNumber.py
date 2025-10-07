# https://leetcode.com/problems/single-number/description/
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Example 1:
# Input: nums = [4,1,2,1,2]
# Output: 4

# time - complexity - O(n)
# space - complexity - O(no of unique elements in list)
def findSingleNumber1(nums):
    count = dict()

    for i in nums:
        count[i] = count.setdefault(i, 0) + 1

    for key in count.keys():
        if(count[key] == 1):
            return key
    return -1

# xor of a number with itself always gives zero
# if there is only one number in list with count as 1 and other with count as 2
# then xor of all the numbers in the list will be that single number
# time - complexity - O(n)
# space - complexity - O(1)
def findSingleNumberUsingXOR(nums):
    xor = 0
    for i in nums:
        xor = xor ^ i
    
    return xor

nums = [4,1,2,1,2]
print(f"Single number in {nums}:", findSingleNumber1(nums))
print(f"Single number in {nums} using xor", findSingleNumberUsingXOR(nums))


