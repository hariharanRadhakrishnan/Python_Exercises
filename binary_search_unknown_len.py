"""
Binary sort of a sorted (ascending) lst with unknown length
"""
def binarySearch(lst, start, end, ele):
	while True:
		if (start == end):
			if (lst[start] == ele):
				return start
			else:
				# print ("BinFunction__Ouput1")
				return -1
		elif (end-1 == start):
			if (lst[start] == ele):
				return start
			elif (lst[end] == ele):
				return end
			else:
				# print ("BinFunction__Ouput2")
				return -1

		mid = (start+end)//2
		if(lst[mid] >= ele):
			end = mid
		else:
			if(lst[mid+1] == ele):
				return mid+1
			else:
				start = mid


def findEle(lst, ele):
	start = end = 0
	try:
		while (lst[end] < ele):
			start = end
			end = (start+1)*2
	except IndexError:
		for i in range(end,start-1,-1):
			try:
				if (lst[i] >= ele):
					end = i
					break
				else:
					# print ("IndexError__Ouput")
					# even returning outisde try catch runs the finally block!!!
					#return -1 #doesn't return out of the function!!! Suprised
					end = start
					break
			except IndexError:
				pass		
	finally:
		return binarySearch(lst, start, end, ele)
	return None

lst = [1,2,3,3,4,5,6,6,6,6,7,8,9,10,11,11,11,11,11,15,15,15,16,20]
str1 =''
str2 =''
for ind,ele in enumerate(lst):
	str1 += str(ele) + " "*(4-len(str(ele)))
	str2 += str(ind) + " "*(4-len(str(ind)))

print("elems: ", str1)
print("index: ", str2)
print()
print ("ele: ", 10, "\tAns: ",findEle(lst, 10), "\tReqAns: ",13)
print ("ele: ", 11, "\tAns: ",findEle(lst, 11), "\tReqAns: ",14)
print ("ele: ", 6, "\tAns: ", findEle(lst, 6), "\tReqAns: ",6)
print ("ele: ", 20, "\tAns: ", findEle(lst, 20), "\tReqAns: ",23)
print ("ele: ", 100, "\tAns: ", findEle(lst, 100), "\tReqAns: ",-1)
print ("ele: ", 12, "\tAns: ", findEle(lst, 12), "\tReqAns: ",-1)
