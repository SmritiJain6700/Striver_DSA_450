# time - complexity - O(n/2) ~ O(n)
# space - complexity - O(n/2) ~`O(n) (recurive depth)
def checkPalindromeNumber(n):
    s = str(n)
    return checkPalindrome(0, len(s)-1 , s)

def checkPalindrome(left, right, s):
    if(left >= right):
        return True
    
    if(s[left] != s[right]):
        return False
    return checkPalindrome(left+1, right-1, s)


n = int(input("Enter a number:"))
print(f"{n} is Palindrome: ", checkPalindromeNumber(n))