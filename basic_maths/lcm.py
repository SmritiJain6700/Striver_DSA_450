# time - complexity analysis 
# we are going g 2g 3g ... (a*b)
# so number of iterations that can happen is (a*b)/g and g = max(a,b) therefore no of iterations = min(a,b)
# so time complexity - O(min(a,b))
# space complexity - O(1)
def lcm1(a, b):
    # find the smaller value
    s = min(a,b)

    # find the larger value
    g = max(a, b)

    for i in range(g, (a*b) + 1, g):
        if(i % s == 0):
            return i
    return a*b

# since lcm(a,b) * gcd(a,b) = (a*b) therefore lcm(a,b) = (a*b)/gcd(a,b)
# time complexity - O(log min(a,b))
# space complexity - O(log min(a,b))

def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b, a%b)
    
def lcm2(a,b):
    if(a == b):
        return a
    else:
        return (a*b)//gcd(a,b)

a = int(input("Enter the first no:"))
b = int(input("Enter the second no:"))
print(f"The lcm of {a} and {b} using method 1 is: {lcm1(a, b)}")
print(f"The lcm of {a} and {b} using method 2 is: {lcm2(a, b)}")
