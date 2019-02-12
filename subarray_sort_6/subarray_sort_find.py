"""
Given an array of integers, find the continuous subarray, which when sorted, 
results in the entire array being sorted. 
For example: A = [0,2,5,3,1,8,6,9], result is the subarray [2,5,3,1,8,6]
because, [2,5,3,1,8,6] when sorted => [1,2,3,5,8,6] will result in [0,1,2,3,5,8,6,9]

[1,2,4,5,3,5,6,7,9] --> [4,5,3] - If you sort from indices 2 to 4, the entire array is sorted.
[1,3,5,2,6,4,7,8,9] --> [3,5,2,6,4] - indices 1 to 5

"""

def find_subarray(lst):
	start = 0
	end = len(lst) - 1
	if(end == -1):
		return lst

	while (end-1 > -1 and lst[end] > lst[end-1]):
		end -= 1

	if (end == 0):
		return []

	while (start+1 < len(lst) and lst[start] < lst[start+1]):
		start += 1

	bigVal = lst[end-1]
	smallVal = lst[start+1]
	
	while (end < len(lst) and lst[end] < bigVal):
		end += 1

	while (start > -1 and smallVal < lst[start]):
		start -= 1

	return lst[start+1:end]


lst =  [0,2,5,3,1,8,6,9]
print(lst)
print(find_subarray(lst), "\n")


lst =  [1,2,4,5,3,5,6,7,9]
print(lst)
print(find_subarray(lst), "\n")

lst =  [1,3,5,2,6,4,7,8,9]
print(lst)
print(find_subarray(lst), "\n")


lst =  [2,3,4,1,8,5,6,7,9]
print(lst)
print(find_subarray(lst), "\n")

lst =  [1,2,3,4,5,6,7,9]
print(lst)
print(find_subarray(lst), "\n")

lst =  []
print(lst)
print(find_subarray(lst), "\n")