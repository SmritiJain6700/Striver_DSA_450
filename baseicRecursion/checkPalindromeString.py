# time-complexity = O(n/2) ~ O(n) no of recursive calls = O(n/2)
# space-complexity = O(n/2) ~ O(n) recursive stack spacegit
# OOP logic
class Palindrome:
    def __init__(self, s):
        self.s = s
    
    def checkPalindrome(self, start, end):
        if(start >= end):
            return True
        
        if(self.s[start] != self.s[end]):
            return False
        else:
            return self.checkPalindrome(start + 1, end - 1)
        
def checkPalindrome(s, start, end):
    if(start >= end):
        return True
    
    if(s[start] != s[end]):
        return False
    else:
        return checkPalindrome(s, start+1, end-1)
    
# oops way
s = input()
print("OOPS")
obj = Palindrome(s)
print(obj.checkPalindrome(0, len(s)-1))

# simple function way
s1 = input()
print("Simple")
print(checkPalindrome(s1, 0, len(s1)-1))
