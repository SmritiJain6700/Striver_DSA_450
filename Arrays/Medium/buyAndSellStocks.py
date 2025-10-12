# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# time - complexity - O(n**2)
# space - complexity - O(1)
def bestTimeToBuyAndSellStocks1(nums):
    maxProfit = 0
    n = len(nums)

    for i in range(0,n):
        for j in range(i+1,n):
            x = nums[j] - nums[i]
            if(x > maxProfit):
                maxProfit = x
    return maxProfit

# time - complexity - O(n)
# space - complexity - O(1)
def bestTimeToBuyAndSellStocks2(nums):
    n = len(nums)
    maxProfit = 0
    minn = nums[0]

    for i in range(1, n):
        maxProfit = max(maxProfit, nums[i]-minn)
        if(nums[i] < minn):
            minn = nums[i]

    return maxProfit

nums = [7,1,5,3,6,4]
print(f"Maximum profit achieved after buying and selling stocks from {nums} using brute force approach: ", bestTimeToBuyAndSellStocks1(nums))
print(f"Maximum profit achieved after buying and selling stocks from {nums} using optimal approach: ", bestTimeToBuyAndSellStocks2(nums))