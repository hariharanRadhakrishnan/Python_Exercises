import re
import sys
import os

def openFile(fileName, fileMode):
	try:
		file = open(fileName, fileMode)
	except:
		return None
	else:
		return file

def changeDir(path):
	try:
		print("..... Changing directory to", path)
		os.chdir(path)
	except:
		print("FAILED,",path, "does not exist")
		return

def createOutDir():	
	try:
		print("..... Creating Output folder, small_configs")
		os.mkdir("small_configs")
	except:
		print("small_configs already exists")
	finally:
		changeDir("small_configs")

def generateSmallConfigs(big_file, prefix="sml_config"):
	readVal = big_file.readline()
	fileNum = 1
	new_file = True
	while readVal:
		if (new_file):
			print("..... Creating {0}_{1}.txt".format(prefix,fileNum))
			small_file = openFile("{0}_{1}.txt".format(prefix,fileNum),"w")
			new_file = False
		small_file.write(readVal)
		if(re.match(r"^[!]",readVal)):
			small_file.close()
			fileNum += 1
			new_file = True
		if(re.findall(r"AWS_DualDC",readVal)):
			print("{0}_{1}.txt".format(prefix,fileNum))
		readVal = big_file.readline()

def printUsageDetails():
	print("\n###################### USAGE: ######################")
	print("\t1.py [<Big_Config_File> [<Path_to_the_output_dir> [<Output_file_prefix>]]]")

def main():
	if (len(sys.argv)>1):
		print("..... Opening Big Config File,", sys.argv[1])
		big_file = openFile(sys.argv[1],"r")
	else:
		print("..... Opening Big Config File, nsd.txt")
		big_file = openFile("nsd.txt", "r")
	if(big_file == None):
		print ("Error with Big Config File, File not found")
		return 0
	
	if(len(sys.argv)>2):
		changeDir(sys.argv[2])
	createOutDir()

	if(len(sys.argv)>3):
		generateSmallConfigs(big_file, sys.argv[3])
	else:
		generateSmallConfigs(big_file)

	printUsageDetails()


if __name__ == '__main__':
	main()