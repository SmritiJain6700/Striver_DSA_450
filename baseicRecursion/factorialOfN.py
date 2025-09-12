# time-complexity - O(n) (no of recursive calls)
# space-complexity - O(n) (recursive stack space) (depth of recursion = n)
def factorialOfN(n):
    if(n == 0):
        return 1
    return n * factorialOfN(n-1)

print(factorialOfN(4))