# time complexity -- O(2**n) -- no of recursive calls = 2**n
# space complexity -- O(n) -- recursion max goes n level deep -- stack space
def fibonacci(n):
    if(n == 0 or n == 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))