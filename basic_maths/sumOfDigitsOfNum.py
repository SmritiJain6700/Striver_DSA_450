# time - complexity : O(number of digits in a number) = O(log10 n)
# space - complexity : O(1)
class Summ:
    def __init__(self, n):
        self.n = n
    
    def findSumOfDigits(self):
        if(n == 0):
            return 0
        summ = 0
        while (self.n != 0):
            x = self.n % 10
            summ += x
            self.n = self.n//10
        return summ

n = int(input("Enter the digit:"))
obj = Summ(n)
print(f"Sum of digits of {n} : {obj.findSumOfDigits()}")