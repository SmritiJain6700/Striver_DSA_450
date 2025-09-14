def gcd1(a, b):
    if(a == 0):
        return b
    if(b == 0):
        return a 
    if(a == b):
        return a
    if(a > b):
        return gcd1(b, a%b)
    else:
        return gcd1(a, b%a)

a = int(input("Enter digit a:"))
b = int(input("Enter digit b:"))
x = gcd1(a,b)
print(f"GCD of {a} and {b} is {gcd1(a,b)}")

