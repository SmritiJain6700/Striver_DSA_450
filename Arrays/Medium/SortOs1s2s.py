# https://leetcode.com/problems/sort-colors/description/
# Sort an array of 0s, 1s and 2s - Dutch National Flag Problem
# Given an array arr[] consisting of only 0s, 1s, and 2s. 
# The objective is to sort the array, i.e., put all 0s first, then all 1s and all 2s in last.

# This problem is the same as the famous "Dutch National Flag problem". 
# The problem was proposed by Edsger Dijkstra. The problem is as follows:

# Given n balls of colour red, white or blue arranged in a line in random order.
# You have to arrange all the balls such that the balls with the same colours are adjacent with the order of the balls, 
# with the order of the colours being red, white and blue (i.e., all red coloured balls come first then the white coloured balls and then the blue coloured balls). 

# Examples:

# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: [0, 0, 1, 1, 2, 2] has all 0s first, then all 1s and all 2s in last.


# brute force approach
# time - complexity - O(nlogn)
# space - complexity - O(1)
def sort012(nums):
    nums.sort()


# Better Approach
# using two passes
# time - complexity - O(n) + O(n) = O(2n) ~ O(n)
# space - complexity - O(1)
def sortO12UsingBetterApproach(nums):
    zeroes = 0
    ones = 0
    twos = 0

    for i in nums:
        if(i == 0):
            zeroes += 1
        elif(i == 1):
            ones += 1
        else:
            twos += 1

    ind = 0
    for i in range(zeroes):
        nums[ind] = 0
        ind += 1
    
    for i in range(ones):
        nums[ind] = 1
        ind += 1
    
    for i in range(twos):
        nums[ind] = 2
        ind += 1

# Optimal Approach
# using one passe
# time - complexity - O(n)  
# space - complexity - O(1)
def sortO12UsingOptimalApproach(nums):
    i = 0
    k = len(nums)-1
    j = 0

    while(j <= k):
        if(nums[j] == 0):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif(nums[j] == 1):
            j += 1
        else:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1

nums = [0, 1, 2, 0, 1, 2]
sort012(nums)
print(f"Sort 0s 1s and 2s in {nums} using brute force approach: ", nums)
nums = [0, 1, 2, 0, 1, 2]
sortO12UsingBetterApproach(nums)
print(f"Sort 0s 1s and 2s in {nums} using better approach: ", nums)
nums = [0, 1, 2, 0, 1, 2]
sortO12UsingOptimalApproach(nums)
print(f"Sort 0s 1s and 2s in {nums} using optimal approach: ", nums)