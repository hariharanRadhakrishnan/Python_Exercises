def first_squareroot(num):
	return num**(1/2)


print(first_squareroot(4))
print(first_squareroot(9))
print(first_squareroot(25))

print(first_squareroot(40.4))

print(first_squareroot(0.04))
print(first_squareroot(0.09))
print(first_squareroot(0.25))
print(first_squareroot(-4))
print(first_squareroot(-1))       

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

def second_squareroot(num):
	sign = 1
	if(num < 0):
		return 0
	num = abs(num)
	if (num < 1):
		stopNum = num*100
	else:
		stopNum	= num/2
	for i in nextNum(0,stopNum,0.01):
		if (i**2 < num):
			retVal = i
		else:
			return i*sign
	return 0

print()
# print(second_squareroot(4))
# print(second_squareroot(9))
# print(second_squareroot(25))

# print(second_squareroot(40.4))

# print(second_squareroot(0.04))
# print(second_squareroot(0.09))
# print(second_squareroot(0.25))
# print(second_squareroot(-4))
# print(second_squareroot(-1))
print(second_squareroot(69.72316))