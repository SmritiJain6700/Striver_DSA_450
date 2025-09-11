from functools import reduce

# time complexity : O(n)
# space complexity : O(1)
# my method
def binaryToDecimal(s):
    rbs = s[::-1]
    decimal = 0
    for i in range(0, len(rbs)):
        decimal = decimal + int(rbs[i]) * (2**i)

    return decimal

# time complexity : O(n)
# space complexity : O(1)
def binaryToDecimal2(s):
    decimal = 0
    for digit in s:
        decimal = decimal * 2 + int(digit)
    return decimal

def binaryToDecimalUsingReduce(s):
    return reduce(lambda acc, digit: acc * 2 + int(digit), s, 0)


x = binaryToDecimal("1100")
print("binaryToDecimal first method",x)  
y = binaryToDecimal2("1100")
print("binaryToDecimal second method",y) 
z = binaryToDecimalUsingReduce("1100")
print("binaryToDecimal using reduce",z) 





