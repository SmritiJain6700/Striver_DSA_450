# time - complexity - O(n)
# space - complexity - O(no of unique element in array) ~ O(n)
def findMostFrequentElementInArray(arr):
    countA = dict()
    for i in arr:
        if(countA.get(i,-1) == -1):
            countA[i] = 0
        countA[i] += 1

    maxx = countA[arr[0]]
    val = arr[0]
    for i in range(1, len(arr)):
        if(countA[arr[i]] > maxx):
            maxx = countA[arr[i]]
            val = arr[i]
    return [val,maxx]

arr = [1,1,3,3,3,6,7,9,9,10,-1,-1,-1,-1,-1]
highestFreqElement = findMostFrequentElementInArray(arr)
print("highestFreqElement", highestFreqElement[0], highestFreqElement[1])

