# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

# time - complexity - O(n) + O(n) = O(2n) ~ O(n)
# space - complexity - O(n)
def rearrangeArrayUsingBruteForce(nums):
    n = len(nums)
    ans = [0]*n
    pos = list()
    neg = list()

    for i in range(0, n):
        if(nums[i] < 0):
            neg.append(nums[i])
        else:
            pos.append(nums[i])
        
    for i in range(0, n//2):
        ans[i*2] = pos[i]
    
    for j in range(0, n//2):
        ans[j*2+1] = neg[j]

    return ans

# time - complexity - O(n) 
# space - complexity - O(n)
def rearrangeArrayUsingApproach2(nums):
    n = len(nums)
    ans = [0]*n
    pos = 0
    neg = 1

    for i in range(0, n):
        if(nums[i] < 0):
            ans[neg] = nums[i]
            neg += 2
        else:
            ans[pos] = nums[i]
            pos += 2

    return ans

nums = [3,1,-2,-5,2,-4]
print(f"Rearranging element of {nums} using brute force approach give: ", rearrangeArrayUsingBruteForce(nums))
print(f"Rearranging element of {nums} using approach 2 give: ", rearrangeArrayUsingApproach2(nums))


