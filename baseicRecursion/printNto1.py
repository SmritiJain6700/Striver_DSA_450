# time complexity - O(n) -- no of recursive calls - O(n)
# space complexity - O(n) -- recursive stack space - O(n) - depth of recursion
class PrintNto1:
    def __init__(self, n):
        self.n = n
    
    def printNto1(self):
        if(self.n == 0):
            return
        print(self.n, end = " ")
        self.n -= 1
        self.printNto1()

def printNto1(N):
    if(N == 0):
        return
    print(N, end = " ")
    printNto1(N-1)

# using oops
obj = PrintNto1(5)
print("Using oops method")
obj.printNto1()

# using simple function
print("\nUsing simple function")
printNto1(6)
