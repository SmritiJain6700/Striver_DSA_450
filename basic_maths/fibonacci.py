# time complexity - O(n)
# space complexity - O(1)
def fibonacci(n):
    if(n == 0 or n == 1):
        return n
    a = 0
    b = 1
    for n in range(2,n+1):
        c = a + b
        a = b
        b = c
    return c

n = int(input())
print(fibonacci(n))

