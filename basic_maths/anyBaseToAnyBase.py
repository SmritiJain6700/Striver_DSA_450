def toDecimal(s, fromBase):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decimal = 0
    s = s.upper() # to handle both A-Z and a-z

    for char in s:
        val = digits.index(char)
        decimal = decimal * fromBase + val
    
    return decimal

def fromDecimal(decimal, toBase):
    if(decimal == 0):
        return "0"
    
    val = ""
    while(decimal > 0):
        x = decimal%toBase
        val = str(x) + val
        decimal = decimal//toBase
    return val

def anyBaseToAnyBase(s, fromBase, toBase):
    decimal = toDecimal(s, fromBase)
    val = fromDecimal(decimal, toBase)
    return val

print(anyBaseToAnyBase("A3", 16, 2))