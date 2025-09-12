# time-complexity = O(n/2) ~ O(n) no of recursive calls = O(n/2)
# space-complexity = O(n/2) ~ O(n) recursive stack space
# OOP logic
class ArrayReverse:
    def __init__(self, arr):
        self.arr = arr
    
    def reverse(self, start, end):
        if(start >= end):
            return 
        
        self.arr[start], self.arr[end] = self.arr[end], self.arr[start]
        self.reverse(start+1, end-1)

def reverse(arr, start, end):
    if(start >= end):
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse(arr, start+1, end-1)

# oops way
arr = [1,2,3,4]
obj = ArrayReverse(arr)
obj.reverse(0, len(arr)-1)
print(arr)

# simple function way
arr1 = [1,2,3,4,5]
reverse(arr1, 0, len(arr1)-1)
print(arr1)
