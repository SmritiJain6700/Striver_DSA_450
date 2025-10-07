# https://www.geeksforgeeks.org/dsa/union-of-two-arrays/
# You are given two arrays a[] and b[], return the Union of both the arrays in any order.

# The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

# Note: Elements of a[] and b[] are not necessarily distinct.
# Note that, You can return the Union in any order 
# Examples:
# Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
# Output: [1, 2, 3]
# Explanation: Union set of both the arrays will be 1, 2 and 3.

# time - complexity - O(n+m)
# space - complexity - no of unique elements
def unionTwoArrays(a, b):
    visited = set()

    ans = list()

    for i in a:
        if(i not in visited):
            ans.append(i)
            visited.add(i)

    for j in b:
        if(j not in visited):
            ans.append(j)
            visited.add(j)

    return ans

a =  [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(f"Union of {a} and {b} is:", unionTwoArrays(a,b))
