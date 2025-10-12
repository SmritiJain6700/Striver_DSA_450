# https://leetcode.com/problems/majority-element/description/
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# brute force approach
# use two loops
# time - complexity - O(n**2)
# space - complexity - O(1)
def majorityEelementUsingBFA(nums):
    n = len(nums)

    for i in range(0, n):
        count = 0
        for j in range(0,n):
            if(nums[i] == nums[j]):
                count += 1
        if(count > n//2):
            return nums[i]
    return -1

# using hashMap
# time - complexity - O(n)
# space - complexity - O(n)
def majorityElementUsingHashMap(nums):
    countMap = dict()
    n = len(nums)
    for i in nums:
        countMap[i] = countMap.get(i, 0) + 1
        if(countMap[i] > n//2):
            return i
    return -1

# vimp
# Boyer-Moore voting algorithm is one of the popular optimal algorithms which is used to find 
# the majority element among the given elements that have more than N/ 2 occurrences.
# Intuition
# When we see the same element as the candidate, we increase its votes; when we see a different one, 
# we decrease them — representing how the candidate’s “lead” weakens against other elements.
# If votes drop to zero, it means equal opposition, so we pick a new candidate.
# The element that survives this process is the majority element (appears more than n/2 times).

# case1: we are sure the list has an majority element
# so we dont need to validate the element calculated from this method
# time - complexity - O(n)
# space - complexity - O(1)
def majorityElementUsingMooreVoting1(nums):
    n = len(nums)
    count = 0
    ele = -1

    for i in nums:
        if(count == 0):
            count = 1
            ele = i
        elif(i == ele):
            count += 1
        else:
            count -= 1
    return ele

# case2: we are not sure the list has an majority element
# so we need to validate the element calculated from this method
# time - complexity - O(n)
# space - complexity - O(1)
def majorityElementUsingMooreVoting2(nums):
    n = len(nums)
    count = 0
    ele = -1

    for i in nums:
        if(count == 0):
            count = 1
            ele = i
        elif(i == ele):
            count += 1
        else:
            count -= 1

    # validate the count
    count = 0
    for i in nums:
        if(i == ele):
            count += 1
    
    if(count > n//2):
        return ele
    
    return -1

nums = [2,2,1,1,1,2,2]  
print(f"Majority element in list {nums} using brute force approach: ", majorityEelementUsingBFA(nums))
print(f"Majority element in list {nums} using hashMap approach: ", majorityElementUsingHashMap(nums))
print(f"Majority element in list {nums} using Boyer-Moore voting algorithm approach when u r sure majority element is present in list: ", majorityElementUsingMooreVoting1(nums))
print(f"Majority element in list {nums} using Boyer-Moore voting algorithm approach when u r not sure majority element is present in list: ", majorityElementUsingMooreVoting2(nums))