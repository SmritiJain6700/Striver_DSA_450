# Given an array of integers and a target value K, print all pairs of elements from the array whose sum is equal to K.
# Each pair should be printed only once, even if there are duplicate numbers in the array.
# Example:
# input:
# arr = [1, 5, 7, -1, 5]
# K = 6
# output:
# (1, 5)
# (7, -1)

# brute force approach 
# using two loops
# time - complexity - O(n**2)
# space - complexity - O(1)
def twoSumUsingBFA(nums, target):
    pairs = set() # to fetch unique pairs

    n = len(nums)
    for i in range(0, n):
        for j in range(i+1, n):
            if((nums[i] + nums[j]) == target):
                pairs.add(tuple(sorted([nums[i], nums[j]])))
    return pairs


# Optimal Appraoch when the input list is unsorted 
# using hashSet
# time - complexity - O(n)
# space - complexity - O(n)
def twoSumUsingHashMap(nums, target):
    hashSet = set()
    pairs = set() # to fetch unique pairs

    n = len(nums)
    for i in range(0, n):
        x = target - nums[i]
        if(x in hashSet):
            pairs.add(tuple(sorted([nums[i], x])))
        hashSet.add(nums[i])
    return pairs

# Two Pointer approach: when the input list is sorted 
# time - complexity - O(nlogn)
# space - complexity - O(1)
def twoSumUsingTwoPointer(nums, target):
    nums.sort()
    pairs = set()

    i = 0
    j = len(nums)-1
    while(i < j):
        x = nums[i] + nums[j]
        if(x == target):
            pairs.add((nums[i], nums[j]))
            i += 1
            j -= 1
        elif(x > target):
            j -= 1
        else:
            i += 1
    return pairs

nums = [1, 5, 7, -1, 5]
target = 6
print(f"The unique pairs in list {nums} giving sum {target} using brute force approach: ", twoSumUsingBFA(nums, target))
print(f"The unique pairs in list {nums} giving sum {target} using hashMap approach: ", twoSumUsingHashMap(nums, target))
print(f"The unique pairs in list {nums} giving sum {target} using two pointer approach: ", twoSumUsingTwoPointer(nums, target))