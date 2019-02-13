"""
problem:
in:[1,2,3,34,4,4,4,4,,5,3,4,324,4,2,52]
in:num
out:[<num, =num, >num]
"""

def divide_list(lst, num):
	start = 0
	end = len(lst)-1
	lessThan = 0
	equalTo = 0
	for i in lst:
		if i < num:
			lessThan += 1
		elif i == num:
			equalTo += 1
			
	lessIndex = start
	equalIndex = lessIndex + lessThan
	lessBound = equalIndex
	equalBound = equalTo + equalIndex
	# greaterIndex = end
	# print(lessIndex, equalIndex, greaterIndex, equalBound)
	while start < lessBound or end > equalBound-1:
		# print(start, end)
		while end > equalBound-1 and lst[end] > num:
			end -= 1
		while start < lessBound and lst[start] < num:
			start += 1
		while equalIndex < equalBound and lst[equalIndex] == num:
			equalIndex += 1
		
		if (start < lessBound or end > equalBound-1):
			if lst[end] < num and lst[start] > num:
				temp = lst[end]
				lst[end] = lst[start]
				lst[start] = temp
				# lessIndex = start
				# greaterIndex = end
				start += 1
				end -= 1
			elif lst[end] == num:
				if equalIndex < equalBound:
					lst[end] = lst[equalIndex]
					lst[equalIndex] = num
					equalIndex += 1
			elif lst[start] == num:
				if equalIndex < equalBound:
					lst[start] = lst[equalIndex]
					lst[equalIndex] = num
					equalIndex += 1
	return lst
	
lst = [1,4,7,13,54,104,454,5,1,6,4,3,100,20,1]
print(lst,7)
print(divide_list(lst, 7))
print()
					
lst = [1,4,7,13,54,104,454,5,1,6,4,3,100,20,1]
print(lst,1)
print(divide_list(lst, 1))
print()

lst = [1,4,7,13,54,104,454,5,1,6,4,3,100,20,1]
print(lst,4)
print(divide_list(lst, 4))
print()