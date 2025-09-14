# Input: n = 200
# Output: 2
# Explanation: By reversing the digits of number, number will change into 2.
# time - complexity - O(number of digits) - O(log10 n)
# space - complexity - O(1)
def reverseNumber(n):
    if(n == 0):
        return 0
    revNum = 0
    while(n != 0):
        revNum = revNum*10 + n%10
        n = n//10
    return revNum

n = int(input("Enter a number:"))
print(f"Reverse of a number-{n} is {reverseNumber(n)}")