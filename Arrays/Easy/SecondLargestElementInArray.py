def secondLargestElementInArrayUsingSorting(arr):
    arr.sort()
    n = len(arr)
    for i in range(n-2,-1,-1):
        # return the first element which is not equal to the largest element
        if(arr[i] != arr[n-1]):
            return arr[i]
    return -1 


def secondLargestElementInArrayUsingTwoPassSearch(arr):
    # in first pass find the largest element in the array
    maxx = float("-inf")
    for i in arr:
        if(i > maxx):
            maxx = i
    
    # in the second pass find the second largest element
    secondMaxx = float("-inf")
    for i in arr:
        if(i > secondMaxx and i < maxx):
            secondMaxx = i

    if(secondMaxx == float("-inf")):
        return -1
    else:
        return secondMaxx
    
def secondLargestElementInArrayUsingOnePassSearch(arr):
    
    maxx = float("-inf")
    
    secondMaxx = float("-inf")
    for i in arr:
        if(i > maxx):
            secondMaxx = maxx
            maxx = i
        elif(i > secondMaxx and i < maxx):
            secondMaxx = i
        else:
            continue

    if(secondMaxx == float("-inf")):
        return -1
    return secondMaxx

arr = [1,10,34,45,67,91,0,100]
print(f"the second largest element in the array using sorting is:", secondLargestElementInArrayUsingSorting(arr))
print(f"the second largest element in the array using two pass search  is:", secondLargestElementInArrayUsingTwoPassSearch(arr))
print(f"the second largest element in the array using one pass search is:", secondLargestElementInArrayUsingOnePassSearch(arr))