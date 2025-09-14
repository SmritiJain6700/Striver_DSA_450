# there will be two ways to do it
from functools import reduce

def countDigits(n):
    if(n == 0):
        return 1
    count = 0
    while(n != 0):
        count += 1
        n = n//10
    return count

def countDigitsUsingReduce(n):
    s = str(n)
    count = reduce(lambda acc, x: acc + 1, s, 0)
    return count

n = int(input("Enter a digit:"))
print(f"Count digits of {n}: {countDigits(n)}")
print(f"Count digits using reduce {n}: {countDigitsUsingReduce(n)}")