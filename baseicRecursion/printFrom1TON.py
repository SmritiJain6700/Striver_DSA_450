# time - complexity - O(n)
# space - complexity - O(n) (recursive stack space) (depth of recursion = n)
def printFrom1TON(n):
    if(n == 0):
        return 
    printFrom1TON(n-1)
    print(n, end=" ")

printFrom1TON(5)