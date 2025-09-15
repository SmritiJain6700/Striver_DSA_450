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