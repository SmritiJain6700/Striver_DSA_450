# Amstrong number 
# A number which is equal to the sum of its digits where the digits 
# are raised to the power of number of digits in the number
# 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 126 + 27 = 153

# time - complexity = O(log10 n) since number of digits = O(log10 n)
# space - complexity = O(log10 n) since number of digits = O(log10 n) -- digits list
class Amstrong:
    def __init__(self, n):
        self.n = n

    def findDigits(self, n):
        x = self.n
        digits = []
        while(x != 0):
            digits.append(x%10)
            x = x//10
        return digits
    
    def checkIfAmstrong(self):
        digits = self.findDigits(self.n)
        count = len(digits)
        amstrongSum = 0
        for digit in digits:
            amstrongSum += digit**count
        if(amstrongSum == self.n):
            return True
        else:
            return False

n = int(input("Enter a digit:"))
obj = Amstrong(n)
print(f"The number {n} is Amstrong: {obj.checkIfAmstrong()}")


