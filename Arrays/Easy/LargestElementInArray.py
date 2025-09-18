# time - complexity - O(n) -- there is a recursive call for each of the elements
# space - complexity - O(n) -- recursive stack depth
def largestUsingRecursion(arr):
    maxx = float("-inf")
    n = len(arr)

    return findLargest(arr, n, maxx)

# time - complexity - O(n) -- as we are traversing over each element
# space - complexity - O(1)
def largestUsingIterativeMethod(arr):
    maxx = float("-inf")
    for i in arr:
        if(i > maxx):
            maxx = i
        else:
            continue
    return maxx

def findLargest(arr, n, maxx):
    if(n == 0):
        return maxx
    
    maxx = max(maxx, arr[n-1])
    return findLargest(arr, n-1, maxx)

arr = [5,10,-1,90]
print(f"Largest element in the array using recursion {arr}: ", largestUsingRecursion(arr))
print(f"Largest element in the array using iterative method {arr}: ", largestUsingIterativeMethod(arr))