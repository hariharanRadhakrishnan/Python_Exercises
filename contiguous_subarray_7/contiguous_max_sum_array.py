'''
Given an array of integers, find the contiguous subarray with the maximum sum. The array can contain both negative and positive integers

'''

def subarray_max_sum(lst):
	start = end = len(lst)-1
	sub_start = end
	sub_end = sub_start + 1
	max_sum = lst[start]
	current_sum = max_sum

	def chech_sum_end():
		nonlocal lst,start,end,sub_start,sub_end,max_sum,current_sum
		check_sum = current_sum
		max_end = end
		while end > start:
			check_sum -= lst[end]
			# print("####", check_sum, lst[end], start, end)
			if check_sum >= current_sum:
				current_sum = check_sum
				max_end = end-1
			end -= 1
		end = max_end

	while start-1 > -1:
		# print("Max: ", max_sum)
		start -= 1
		current_sum += lst[start]
		# print("1. current_sum: ", current_sum)
		chech_sum_end()
		if current_sum >= max_sum:
			max_sum = current_sum
			sub_start = start
			sub_end = end+1
		# print("2. current_sum: ", current_sum, start, end)
	return lst[sub_start:sub_end]

lst = [-100,-1,0,0,-3,-3,4,-41,-2]
print(lst)
lst1 = subarray_max_sum(lst)
print (lst1, sum(lst1), "\n")

lst = [0,1,-5,10,-6,-9,2,0,7]
print(lst)
lst1 = subarray_max_sum(lst)
print (lst1, sum(lst1), "\n")

lst = [0,1,5,10,-6,9,2,-8,7]
print(lst)
lst1 = subarray_max_sum(lst)
print (lst1, sum(lst1), "\n")

lst = [-1,-2,-3,-4]
print(lst)
lst1 = subarray_max_sum(lst)
print (lst1, sum(lst1), "\n")

lst = [1,-8, -9,200, -8,-700, 0, 0, 100]
print(lst)
lst1 = subarray_max_sum(lst)
print (lst1, sum(lst1), "\n")

lst = [1,-8, -9,200, -8,-700, 0, 0, 100]
print(lst)
lst1 = subarray_max_sum(lst)
print (lst1, sum(lst1), "\n")

lst = [1,2,5,-10,13,4,-40,50]
print(lst)
lst1 = subarray_max_sum(lst)
print (lst1, sum(lst1), "\n")