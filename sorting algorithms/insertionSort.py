# Insertion Sort
# this sorting algo works like how we sort playing cards in hand -- picking one card at a time 
# and inserting it into its correct position
# logic
# 1) We divide the array into two parts:
# Sorted part (initially just the first element)
# Unsorted part
# 2) Pick elements one by one from the unsorted part and insert them into their correct position in the sorted part.
# 3) Keep shifting larger elements to the right until the right spot is found.

def insertionSort(arr):
    n = len(arr)

    for i in range(1, n): # start from the 2nd element
        key = arr[i]  # current element to insert
        j = i-1
        # Shift elements of arr[0..i-1] that are > key
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1

        # Insert key at correct position
        arr[j+1] = key
    return arr

# Example
arr = [64, 25, 12, 22, 11]
print("Sorted array:", insertionSort(arr))
