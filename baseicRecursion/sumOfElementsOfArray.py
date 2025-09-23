# time - complexity - O(n) -- because we have one recursive call per element
# space - compleixty - O(n) -- recursive stack depth
def sumOfElementsOfArray(arr):
    n = len(arr)
    return sumOfElements(arr, n)

def sumOfElements(arr, n):
    if(n == 0):
        return 0
    
    return arr[n-1] + sumOfElements(arr, n-1)


arr = [1,2,3,4,5]
print(f"Sum of elements of array {arr}: ", sumOfElementsOfArray(arr))