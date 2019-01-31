def first_cuberoot(num):
	return num**(1/3)


print(first_cuberoot(8))
print(first_cuberoot(27))
print(first_cuberoot(125))
print(first_cuberoot(125))
print(first_cuberoot(1030.301))

print(first_cuberoot(0.008))
print(first_cuberoot(0.027))
print(first_cuberoot(0.125))
print(first_cuberoot(-27))

def nextNum(start,stop,step):
	# print(start,stop,step)
	if(stop < start):
		while(start > stop):
			print(start)
			start = start - step
			yield start
	else:
		while(start < stop):
			start = start + step
			yield start

def second_cuberoot(num):
	sign = 1
	if(num < 0):
		sign = -1
	num = abs(num)
	if (num < 1):
		stopNum = num*1000
	else:
		stopNum	= num//3
	for i in nextNum(0,stopNum,0.01):
		if (i**3 < num):
			retVal = i
		else:
			return i*sign
	return 0

print()
print(second_cuberoot(8))
print(second_cuberoot(27))
print(second_cuberoot(125))

print(second_cuberoot(1030.301))

print(second_cuberoot(0.008))
print(second_cuberoot(0.027))
print(second_cuberoot(0.125))
print(second_cuberoot(-27))