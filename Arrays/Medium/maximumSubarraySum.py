# You’re given an array (can have +ve and -ve numbers).
# find the subarray (containing at least one element) 
# which has the maximum possible sum, and return that sum.
# Example:
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6   (from subarray [4, -1, 2, 1])

# using two nested loops
# find sum of all possible subarrays
# checking which subarray has the maximum sum
# time - compleixty - O(n**2)
# space - complexity - O(1)
def maximumSubarraySumUsingBFA(nums):
    n = len(nums)
    maxSum = float("-inf")

    for i in range(0,n):
        summ = 0
        for j in range(i,n):
            summ += nums[j]
            if(summ > maxSum):
                maxSum = summ
    return maxSum


# Kadane's Algo -- used to find maximum sum subarray
# Intuition
# Imagine you are walking through the array, adding numbers one by one to a running total (current_sum).
# Now think —
# if current_sum becomes negative, will it help the future elements?
# ❌ No! Because adding a negative sum to future elements will only make them smaller.
# So whenever the running sum goes below 0, you reset it to 0 — meaning:
# “Forget the past, start fresh from the next element.”
# While doing this, you also keep track of the maximum sum you’ve ever seen so far (max_sum).

# time - complexity - O(n)
# space - complexity - O(1)
def maximumSubarraySumUsingKadaneAlgo(nums):
    n = len(nums)
    summ = 0
    maxSum = float("-inf")

    for i in nums:
        summ += i
        maxSum = max(maxSum, summ)
        if(summ < 0):
            summ = 0

    return maxSum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum subarray sum in list {nums} using brute force approach: ", maximumSubarraySumUsingBFA(nums))
print(f"Maximum subarray sum in list {nums} using Kadane's Algo: ", maximumSubarraySumUsingKadaneAlgo(nums))