# https://leetcode.com/problems/max-consecutive-ones/description/
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# time - complexity - O(n)
# space - complexity - O(1)
def maxConsecutiveOnes(nums):
    count = 0
    maxCount = float("-inf")

    n = len(nums)
    for i in range(0,n):
        if(nums[i] == 1):
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 0

    maxCount = max(maxCount, count)
    return maxCount

nums = list(map(int, input("Enter the input elements:").split(" ")))
print(f"The max consecutive one in {nums} are:", maxConsecutiveOnes(nums))