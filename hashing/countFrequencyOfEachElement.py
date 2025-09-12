# time - complexity - O(n)
# space - complexity - O(noofuniqueelementinarray) ~ O(n) --> dict space
def countFrequencyOfEachElement(arr):
    countA = dict()
    for element in arr:
        if(countA.get(element,-1) == -1):
            countA[element] = 0
        countA[element] += 1
    
    return countA

arr = [1,3,3,1,1,0,0,1]
freq = countFrequencyOfEachElement(arr)
print(freq)
