# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# time - complexity - O(n)
# space - compleixty - O(1)

def removeDuplicatesInPlaceUsing3Pointers(arr):
    ind = 1 #holds the index of the next distinct item
    k = 0
    j = 1

    n = len(arr)
    while(j < n):
        if(arr[k] != arr[j]):
            arr[ind] = arr[j]
            ind += 1
            k = j #moving k only when a unique element is found
        j += 1

    return ind

def removeDuplicatesInPlaceUsing2Pointers(arr):
    ind = 1 #holds the index of next distinct item
    n = len(arr)
    for i in range(1,n):
        if(arr[i-1] != arr[i]):
            arr[ind] = arr[i]
            ind += 1
    return ind

arr = list(map(int, input("Enter the sorted array with duplicate elements: ").split(",")))
print("No of distinct elements using removeDuplicatesInPlaceUsing3Pointers",removeDuplicatesInPlaceUsing3Pointers(arr))
arr1 =  list(map(int, input("Enter the sorted array with duplicate elements: ").split(",")))
print("No of distinct elements using removeDuplicatesInPlaceUsing2Pointers",removeDuplicatesInPlaceUsing2Pointers(arr1))
    
