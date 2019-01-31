

def first_readfile(file):
		yield file.read()


myfile = open("myfile.txt")
readVal = first_readfile(myfile)
print(readVal)
for i in readVal:
	print(i)
	print("####################")
myfile.close()


def second_readfile(file):
	yield file.read(1)

myfile = open("myfile.txt")
readVal = second_readfile(myfile)
print(readVal)
for i in second_readfile(myfile):
	print(i)
	print("####################")
myfile.close()


def third_readfile(file):
	for line in file:
		yield line

myfile = open("myfile.txt")
readVal = third_readfile(myfile)
print(readVal)
for i in third_readfile(myfile):
	print(i)
	print("####################")
myfile.close()