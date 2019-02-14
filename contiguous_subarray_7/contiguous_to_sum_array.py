'''
Given an array of positive integers, find the contiguous subarray that sums to a given number X
'''

def subarray_to_sum(lst, sumVal):
	start = end = len(lst)-1
	sub_start = sub_end = end
	current_sum = lst[start]

	def check_sumGrt_end():
		nonlocal lst,start,end,sub_start,sub_end,current_sum
		check_sum = current_sum
		max_end = end
		while end > start:
			check_sum -= lst[end]
			# print("####", check_sum, lst[end], start, end)
			if check_sum < current_sum:
				current_sum = check_sum
				max_end = end-1
				break
			end -= 1
		end = max_end

	def check_sumLst_end():
		nonlocal lst,start,end,sub_start,sub_end,current_sum,sumVal
		check_sum = current_sum
		max_end = end
		while end < len(lst)-1:
			end += 1
			check_sum += lst[end]
			# print("####", check_sum, lst[end], start, end)
			if check_sum >= sumVal:
				current_sum = check_sum
				max_end = end
				break
		end = max_end

	while start-1 > -1:
		start -= 1
		current_sum += lst[start]
		# print("1. current_sum: ", current_sum)
		if current_sum > sumVal:
			check_sumGrt_end()
		if current_sum < sumVal:
			check_sumLst_end()
		if current_sum == sumVal:
			sub_start = start
			sub_end = end+1
			break
		# print("2. current_sum: ", current_sum, start, end)
	return lst[sub_start:sub_end]

lst = [1,2,3,4,5,6,7]
print(lst, 10)
lst1 = subarray_to_sum(lst, 10)
print (lst1, sum(lst1), "\n")

lst = [1,3,7,2,5,10,7]
print(lst, 10)
lst1 = subarray_to_sum(lst, 10)
print (lst1, sum(lst1), "\n")

lst = [1,3,7,2,5,10,7]
print(lst, 24)
lst1 = subarray_to_sum(lst, 24)
print (lst1, sum(lst1), "\n")

lst = [1,2,3,7,2,15,9,10,7,15]
print(lst , 27)
lst1 = subarray_to_sum(lst, 27)
print (lst1, sum(lst1), "\n")