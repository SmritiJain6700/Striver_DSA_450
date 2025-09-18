# Merge Sort Algo - https://www.geeksforgeeks.org/dsa/merge-sort/
# Merge sort is a popular sorting algorithm known for its efficiency and stability. 
# It follows the divide-and-conquer approach. 
# It works by recursively dividing the input array into two halves, recursively sorting the two halves and finally merging them back together to obtain the sorted array.

def mergeSort(arr, left, right):
    if(left < right):
        middle = (left + right)//2
        mergeSort(arr, left, middle)
        mergeSort(arr, middle+1, right)
        merge(arr, left, middle, right)


def merge(arr, left, middle, right):
    n1 = middle-left+1
    n2 = right-middle

    l = [0]*n1
    r = [0]*n2

    for i in range(0,n1):
        l[i] = arr[left+i]
    
    for j in range(0, n2):
        r[j] = arr[middle+1+j]

    # merge the two arrays
    i = 0
    j = 0
    k = left
    while(i < n1 and j < n2):
        if(l[i] <=  r[j]):
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    
    while(i < n1):
        arr[k] = l[i]
        i += 1
        k += 1

    while(j < n2):
        arr[k] = r[j]
        j += 1
        k += 1
    

arr = [50,-1,10,2,45,1]
mergeSort(arr, 0, len(arr)-1)
print(f"Printing the sorted array:", arr)
