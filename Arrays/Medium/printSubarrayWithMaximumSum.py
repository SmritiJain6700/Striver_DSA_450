# https://www.geeksforgeeks.org/dsa/print-the-maximum-subarray-sum/
# Given an array arr[], the task is to print the subarray having maximum sum.
# Examples:
# Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
# Output: {7, -1, 2, 3}
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

# Input: arr[] = {-2, -5, 6, -2, -3, 1, 5, -6}
# Output: {6, -2, -3, 1, 5}
# Explanation: The subarray {6, -2, -3, 1, 5} has the largest sum of 7.

# using two nested loops
# find sum of all possible subarrays
# checking which subarray has the maximum sum
# time - compleixty - O(n**2)
# space - complexity - O(1)
def maximumSubarraySumUsingBFA(nums):
    n = len(nums)
    maxSum = float("-inf")
    start = 0
    end = 0

    for i in range(0,n):
        summ = 0
        for j in range(i,n):
            summ += nums[j]
            if(summ > maxSum):
                maxSum = summ
                start = i
                end = j
    return start, end


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

    start = 0
    end = 0
    tempStart = 0 #represents start of a potential subarray
    for i in range(0,n):
        summ += nums[i]
        if(maxSum < summ):
            maxSum = summ
            start = tempStart
            end = i
        if(summ < 0):
            summ = 0
            tempStart = i+1
            
    return start,end

nums = [-2, -5, 6, -2, -3, 1, 5, -6]
ind = maximumSubarraySumUsingBFA(nums)
print(f"Maximum subarray sum in list {nums} using brute force approach: ", nums[ind[0]: ind[1]+1])
ind = maximumSubarraySumUsingKadaneAlgo(nums)
print(f"Maximum subarray sum in list {nums} using Kadane's Algo: ", nums[ind[0]: ind[1]+1])