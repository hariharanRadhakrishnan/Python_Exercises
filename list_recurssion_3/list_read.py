def iterative_read(lst):
	reads = 0
	index_val = 0
	list_len = len(lst)
	while(index_val < list_len and reads < 100):
		reads += 1
		if lst[index_val] == -1:
			break
		else:
			index_val = lst[index_val]
	return reads


l = [1,2,3,4,-1]
print(iterative_read(l))
l = [3,6,4,2,1]
print(iterative_read(l))
l = [1,0]
print(iterative_read(l))


def recursive_read(lst,index_val,lst_len, pre_read):
	if (pre_read >= 100):
		return pre_read
	if (index_val >= lst_len):
		return pre_read
	if (lst[index_val] == -1):
		return pre_read + 1
	else:
		return recursive_read(lst,lst[index_val],lst_len,pre_read+1)

def lst_read(lst):
	return recursive_read(lst,0,len(lst),0)

print()

l = [1,2,3,4,-1]
print(lst_read(l))
l = [3,6,4,2,1]
print(lst_read(l))
l = [1,0]
print(lst_read(l))