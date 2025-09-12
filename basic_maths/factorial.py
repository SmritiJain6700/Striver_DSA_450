from functools import reduce

# time complexity - O(n)
# space complexity - O(1)
def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial

def factorialUsingReduce(n):
    l = [i for i in range(1,n+1)]
    fact = reduce(lambda acc, digit: acc*digit, l)
    return fact

n = int(input())
fact = factorial(n)
print(fact)
print("factorial using reduce", factorialUsingReduce(n))