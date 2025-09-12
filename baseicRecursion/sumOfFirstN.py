# time - complexity - O(n)
# space - complexity - O(n) (recursive stack space)(depth of recursion = n)
def sumofFirstN(n, summ):
    if(n == 0):
        return summ
    summ += n
    return sumofFirstN(n-1, summ)

print(sumofFirstN(3,0))