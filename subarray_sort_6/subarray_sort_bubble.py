"""
Given an array of integers, find the continuous subarray, which when sorted, 
results in the entire array being sorted. 
For example: A = [0,2,5,3,1,8,6,9], result is the subarray [2,5,3,1,8,6]
because, [2,5,3,1,8,6] when sorted => [1,2,3,5,8,6] will result in [0,1,2,3,5,8,6,9]

[1,2,4,5,3,5,6,7,9] --> [4,5,3] - If you sort from indices 2 to 4, the entire array is sorted.
[1,3,5,2,6,4,7,8,9] --> [3,5,2,6,4] - indices 1 to 5

"""

def findsubarray(lst):
    start = end = 0
    if (not lst):
        return lst
    
    ind  = 0
    bigVal = lst[ind]
    while (ind+1 < len(lst)):
        if(lst[ind+1] < bigVal):
            end = ind+1
        else:
            bigVal = lst[ind+1]
        ind += 1
    if (end == 0):
        return []

    smallVal = lst[ind]
    while (ind-1 > -1):
        if (lst[ind-1] > smallVal):
            start = ind-1
        else:
            smallVal = lst[ind-1]
        ind -=1
    return lst[start:end+1]
    
lst =  [0,2,5,3,1,8,6,9]
print(lst)
print(findsubarray(lst), "\n")


lst =  [1,2,4,5,3,5,6,7,9]
print(lst)
print(findsubarray(lst), "\n")

lst =  [1,3,5,2,6,4,7,8,9]
print(lst)
print(findsubarray(lst), "\n")


lst =  [2,3,4,1,8,5,6,7,9]
print(lst)
print(findsubarray(lst), "\n")

lst =  [1,2,3,4,5,6,7,9]
print(lst)
print(findsubarray(lst), "\n")

lst =  []
print(lst)
print(findsubarray(lst), "\n")