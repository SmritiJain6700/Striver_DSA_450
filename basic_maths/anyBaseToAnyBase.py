# k = no of digits in s
# time complexity - O(k)
# space complexity - O(1)
def toDecimal(s, fromBase):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decimal = 0
    s = s.upper() # to handle both A-Z and a-z

    for char in s:
        val = digits.index(char)
        decimal = decimal * fromBase + val
    
    return decimal

# time complexity - O(log{tobase}decimal)
# space complexity - O(1)
def fromDecimal(decimal, toBase):
    if(decimal == 0):
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = ""
    while(decimal > 0):
        x = decimal%toBase
        val = digits[x] + val
        decimal = decimal//toBase
    return val

def anyBaseToAnyBase(s, fromBase, toBase):
    decimal = toDecimal(s, fromBase)
    val = fromDecimal(decimal, toBase)
    return val

print(anyBaseToAnyBase("A3", 16, 2))
print(fromDecimal(255, 16))  