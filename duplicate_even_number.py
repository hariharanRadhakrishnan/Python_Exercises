def duplicate1(lst):
	new_lst = list()
	for i in lst:
		if i % 2 == 0:
			new_lst.append(i)
			new_lst.append(i)
		else:
			new_lst.append(i)
	return new_lst

lst = [1,2,3,4]
print(duplicate1(lst))

lst = [1,3,5]
print(duplicate1(lst))

lst = [2,4,6]
print(duplicate1(lst))

lst = []
print(duplicate1(lst))



def duplicate2(lst):
	l = len(lst)
	next_step = 0
	for i in range(l):
		val = lst[i+next_step]
		if(val % 2 == 0):
			next_step += 1
			lst.insert(i+next_step, val) 
	return lst

print()
lst = [1,2,3,4]
print(duplicate2(lst))

lst = [1,3,5]
print(duplicate2(lst))

lst = [2,4,6]
print(duplicate2(lst))

lst = []
print(duplicate2(lst))