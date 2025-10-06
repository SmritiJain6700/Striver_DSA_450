# https://leetcode.com/problems/missing-number/description/

# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# first method -- brute force
# time - complexity - O(n**2)
# space - complexity - O(1)

def usingLinearSearch(nums):
    n = len(nums)
    for i in range(0, n+1):
        if(i not in nums):
            return i
    return -1

# using hashing
# time - complexity - O(n)
# space - compleixty - O(n)
def usingHashing(nums):
    # i will convert it into a set
    # O(n)
    s = set(nums)

    n = len(nums)
    for i in range(0, n+1):
        if(i not in nums):
            return i
    return -1

# using sum of numbers
# time - complexity - O(n)
# space - complexity - O(1)
def usingSumOfNum(nums):
    # calculate sum of all the numbers present in nums 
    summ = 0
    for i in nums:
        summ += i
    
    # calculate summ of all the whole numbers from [0,n]
    n = len(nums)
    summOfWholeNum = 0
    for i in range(0, n+1):
        summOfWholeNum += i


    return summOfWholeNum - summ

# vimp 
# XOR of a number with itself is 0 i.e. x ^ x = 0. This means that the result of XOR of 
# first n natural numbers with the XOR of all the array elements will be the missing number. 
# missing no = (XOR of first n whole no) (xor) (XOR of array elements)
# time - complexity - O(n)
# space - complexity - O(1)
def usingXOR(nums):
    xor1 = 0
    xor2 = 0
    n = len(nums)
    for i in range(0,n+1):
        xor1 ^= i

    for i in nums:
        xor2 ^= i

    return xor1 ^ xor2



nums = list(map(int, input("Enter the input array:").split(" ")))
print("Using Brute force find the missing number is:", usingLinearSearch(nums))
print("Using hashing find the missing number is:", usingHashing(nums))
print("Using sum find the missing number is:", usingSumOfNum(nums))
print("Using sum find the missing number is:", usingXOR(nums))