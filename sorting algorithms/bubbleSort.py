# Bubble sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
# After each pass, the largest element "bubbles up" to the end of the list.
# Repeat until no swaps are needed.
# time complexity - O(n**2)
# space - complexity - O(1)
# stable sort (two equal elements in the sorted array are at the same order as they were in input array) - yes
# inplace sort (doesn’t require extra memory proportional to input size) - yes
def bubbleSort(arr):
    # get the length of the array
    n = len(arr)

    # traverse over all the elements
    for i in range(0,n):
        swapped = False
        # last i elements are already sorted
        for j in range(0,n-i-1):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if(swapped == False):
            break
    return arr

arr = [3,11,4,56,0,98]
sorted_arr = bubbleSort(arr)
print(sorted_arr)