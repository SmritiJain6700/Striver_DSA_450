# Linear Search Algorithm is a searching algorithm
'''In Linear Search, we iterate over all the elements of the array and check if it the current element is equal to the target element. 
If we find any element to be equal to the target element, then return the index of the current element.
Otherwise, if no element is equal to the target element, then return -1 as the element is not found. 
Linear search is also known as sequential search.'''

# time - complexity - O(n)
# space - complexity - O(1)
def linearSearch(arr, target):
    n = len(arr)

    for i in range(0, n):
        if(arr[i] == target):
            return i
    return -1


