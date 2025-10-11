# https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# brute force
# use two loops to iterate over the list and find indexes where the value sum is equal to
# target
# time - complexity -- O(n**2)
# space - complexity -- O(1)
def twoSumBruteForce(nums : list, target : int) -> list:
    n = len(nums)
    for i in range(0, n):
        for j in range(i+1, n):
            if((nums[i] + nums[j]) == target):
                return [i, j]
    return list()

# hashMap Approach -- Optimal Approach -- for unsorted arrays
# time - complexity - O(n)
# space - complexity - O(n)
def twoSumUsingHashMap(nums, target):
    hashMap = dict()

    for i in range(0, len(nums)):
        x = target - nums[i]
        if(x in hashMap):
            return [i, hashMap[x]]
        hashMap[nums[i]] = i

    return list()

# two pointer approach --- optimal approach -- for sorted arrays
# time - complexity - O(n)
# space - complexity - O(1)
def twoSumUsingTwoPointer(nums, target):
    i = 0
    j = len(nums)-1
    while(i < j):
        summ = nums[i] + nums[j]
        if(summ == target):
            return [i,j]
        elif(summ > target):
            j -= 1
        else:
            i += 1
    return list()
        

nums = [2,7,11,15]
target = 13
print(f"The indexes in list {nums} giving sum {target} using brute force approach: ", twoSumBruteForce(nums, target))
print(f"The indexes in list {nums} giving sum {target} using optimal approach 1: ", twoSumUsingHashMap(nums, target))
print(f"The indexes in list {nums} giving sum {target} using optimal approach 2: ", twoSumUsingTwoPointer(nums, target))