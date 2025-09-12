# Time Complexity = O(n)
# Space Complexity = O(n) (recursive stack space as depth of recursion is n)
def printNtimes(n):
    if(n == 0):
        return
    print("GFG", end = " ")
    printNtimes(n-1)

printNtimes(5)