# Linear Search Algorithm is a searching algorithm
'''In Linear Search, we iterate over all the elements of the array and check if it the current element is equal to the target element. 
If we find any element to be equal to the target element, then return the index of the current element.
Otherwise, if no element is equal to the target element, then return -1 as the element is not found. 
Linear search is also known as sequential search.'''

# time - complexity - 
# bestcase T.C  -- the target element is present at the first index - O(1)
# worstCase T.C -- the target element is present at the last index - O(n) 
# space - complexity - O(1)
def linearSearch(arr, target):
    n = len(arr)

    for i in range(0, n):
        if(arr[i] == target):
            return i
    return -1


'''Applications of Linear Search Algorithm:
1) Unsorted Lists: When we have an unsorted array or list, linear search is most commonly used to find any element in the collection.
2) Small Data Sets: Linear Search is preferred over binary search when we have small data sets.
3) Searching Linked Lists: In linked list implementations, linear search is commonly used to find elements within the list. Each node is checked sequentially until the desired element is found.'''

'''Advantages of Linear Search Algorithm:
1) Linear search can be used irrespective of whether the array is sorted or not. It can be used on arrays of any data type.
2) Does not require any additional memory.
3) It is a well-suited algorithm for small datasets.

Disadvantages of Linear Search Algorithm:
1) Linear search has a time complexity of O(N), which in turn makes it slow for large datasets.
2) Not suitable for large arrays.'''


