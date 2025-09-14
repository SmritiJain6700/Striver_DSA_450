def isPalindrome(n):
    if(n == 0):
        return True
    x = n
    revNum = 0
    while(x != 0):
        revNum = revNum*10 + x%10
        x = x//10
    
    if(revNum == n):
        return True
    else:
        return False
    
n = int(input("Enter a number:"))
print(f"The number {n} is palindrome: {isPalindrome(n)}")