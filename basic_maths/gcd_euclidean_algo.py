# Euclidean Algorithm (to calculate gcd or hcf of two numbers a and b)
# time complexity - O(log min(a,b))
# space xomplexity - O(log min(a,b)) -- recursive stack space

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

def gcd2(a,b):
    if(b == 0):
        return a
    else:
        return gcd2(b, a%b)

a = int(input("Enter digit a:"))
b = int(input("Enter digit b:"))
print(f"GCD of {a} and {b} using method1 is {gcd1(a,b)}")
print(f"GCD of {a} and {b} using method2 is {gcd2(a,b)}")

