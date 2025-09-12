# time complexity -- O(2**n) -- no of recursive calls = 2**n
# space complexity -- O(n) -- recursion max goes n level deep -- stack space
def fibonnaci(n):
    if(n == 0 or n == 1):
        return n
    return fibonnaci(n-1) + fibonnaci(n-2)

print(fibonnaci(5))