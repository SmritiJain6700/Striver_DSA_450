# Given two sorted arrays a[] and b[], where each array may contain duplicate elements , the task is to return the elements in the union of the two arrays in sorted order.
# Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.

# Examples:

# Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
# Output: [1, 2, 3, 4, 5, 6, 7]
# Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7

# time - complexity - O(m + n)
# space - complexity - O(m + n)
def unionUsingDict(a, b):
    n1 = len(a)
    n2 = len(b)

    # creating dict1 to store count of each element of a
    dict1 = dict()
    for i in a:
        dict1[i] = dict1.setdefault(i, 0) + 1

    # creating dict2 to store count of each element of b
    dict2 = dict()
    for j in b:
        dict2[j] = dict2.setdefault(j, 0) + 1

    ans  = list()
    i = 0
    j = 0
    while(i < n1 and j < n2):
        if(a[i] < b[j]):
            ans.append(a[i])
            i += dict1[a[i]]

        elif(a[i] > b[j]):
            ans.append(b[j])
            j += dict2[b[j]]

        else:
            ans.append(a[i])
            i += dict1[a[i]]
            j += dict2[b[j]]
    
    while(i < n1):
        ans.append(a[i])
        i += dict1[a[i]]

    while(j < n2):
        ans.append(b[j])
        j += dict2[b[j]]
    
    return ans

# time - complexity - O(m + n)
# space - complexity - O(1)
def unionWithoutExtraSpace(a, b):
    n1 = len(a)
    n2 = len(b)

    ans = list()
    i = 0
    j = 0
    while(i < n1 and j < n2):
        if(a[i] < b[j]):
            if(len(ans) == 0 or ans[-1] != a[i]):
                ans.append(a[i])
            i += 1
        elif(b[j] < a[i]):
            if(len(ans) == 0 or ans[-1] != b[j]):
                ans.append(b[j])
            j += 1
        else:
            if(len(ans) == 0 or ans[-1] != b[j]):
                ans.append(b[j])
            i += 1
            j += 1

    while(i < n1):
        if(len(ans) == 0 or ans[-1] != a[i]):
            ans.append(a[i])
        i += 1
    
    while(j < n2):
        if(len(ans) == 0 or ans[-1] != b[j]):
            ans.append(b[j])
        j += 1
    
    return ans 


a = [1, 2, 2, 2, 2, 3, 4, 4, 4, 5]
b = [1, 2, 3, 6, 7, 7]
print(f"Union of two sorted arrays {a} and {b} is: ", unionUsingDict(a,b))
print(f"Union of two sorted arrays without using extra space {a} and {b} is: ", unionWithoutExtraSpace(a,b))