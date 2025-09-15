# Selection Sort
# it is a comparison based sorting algorithm
# Selection sort repeatedly selects the smallest element or largest depending on the order from the unsorted portion of the array 
# and places it in its correct position
# steps:
# 1) Divide the array into two parts:
# Sorted part (initially empty)
# Unsorted part (initially the whole array)
# 2) Find the minimum element in the unsorted part.
# 3) Swap it with the first element of the unsorted part.
# 4) Move the boundary of sorted part one step to the right.
# 5) Repeat until the array is sorted.

def selectionSort(arr):
    n = len(arr)
    for i in range(0, n):
        # Assume the ith element is the minimum
        min_ind = i
        for j in range(i+1, n):
            if(arr[min_ind] > arr[j]):
                min_ind = j
        # Swap the found minimum with the ith element
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
    return arr

# Example
arr = [64, 25, 12, 22, 11]
print("Sorted array:", selectionSort(arr))
