# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
# Examples:
# Input: nums = [10, 5, 2, 7, 1, 9],  k=15
# Output: 4
# Explanation:
# The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. Therefore, the length of this sub-array is 4.

# Brute force approach -- go through all the subarrays using 3 loops
# time - complexity - O(n^3)
# space - complexity - O(1)
def findLongestSubArrayWithGivenSum1(nums, K):
    n = len(nums)

    max_len = 0

    for i in range(0, n):
        for j in range(i, n):
            summ = 0
            for k in range(i, j+1):
                summ += nums[k]

            if(summ == K):
                max_len = max(max_len, j-i+1)
                
    return max_len

# Brute force approach -- go through all the subarrays using 2 loops
# time - complexity - O(n^2)
# space - complexity - O(1)
def findLongestSubArrayWithGivenSum2(nums, K):
    n = len(nums)

    max_len = 0

    for i in range(0, n):
        summ = 0
        for j in range(i, n):
            summ += nums[j]

            if(summ == K):
                max_len = max(max_len, j-i+1)
                
    return max_len


# Better force approach -- find the prefix Sum 
# if prefixSum is equal to K
# then return index+1
# else check if prefixSum-K in hashMap then it means we found subarray with sum K
# time - complexity - O(n)
# space - complexity - O(1)
def findLongestSubArrayWithGivenSumUsingPrefixSum(nums, K):
    # to store prefixSum and it corresponding index
    hashMap = dict()

    n = len(nums)

    max_len = 0
    # calculate the prefix_sum
    prefixSum = 0
    for i in range(0, n):
        prefixSum += nums[i]

        if(prefixSum == K):
            max_len = max(max_len, (i+1))
        
        x = prefixSum-K
        if(hashMap.get(x,-1) != -1):
            max_len = max(max_len, i-hashMap[x])

        # dry run case [2, 0, 0, 3] with K = 3 you will understand it
        if(hashMap.get(prefixSum,-1) == -1):
            hashMap[prefixSum] = i
    return max_len

        

nums = [10, 5, 2, 7, 1, 9]
K=15
print(f"Length of Longest subarray with given sum using brute force 1 approach is", findLongestSubArrayWithGivenSum1(nums, K))
print(f"Length of Longest subarray with given sum using brute force 2 approach is", findLongestSubArrayWithGivenSum2(nums, K))
print(f"Length of Longest subarray with given sum using prefix Sum better approach is", findLongestSubArrayWithGivenSumUsingPrefixSum(nums, K))
