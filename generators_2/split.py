import traceback
import sys

def first_split(string, delimiter):
	split_string = list()
	prev_split = 0
	for s in string:
		# traceback.print_stack(file=sys.stdout)
		if s == delimiter:
			split_val = string.index(s, prev_split)
			split_string.append(string[prev_split:split_val])
			prev_split = split_val + 1

	split_string.append(string[prev_split:])
	return split_string

s = "hello how are you?"

print(first_split(s,' '))
print(first_split(s, 'h'))
print(first_split(s, 's'))
print(first_split(s,"?"))


def strChar(string):
	# traceback.print_stack(file=sys.stdout)
	for s in string:
		yield s

def second_split(string, delimiter):
	split_string = list()
	prev_split = 0
	for s in strChar(string):
		if s == delimiter:
			split_val = string.index(s, prev_split)
			split_string.append(string[prev_split:split_val])
			prev_split = split_val + 1

	split_string.append(string[prev_split:])
	return split_string

s = "hello how are you?"

print()
print(second_split(s,' '))
print(second_split(s, 'h'))
print(second_split(s, 's'))
print(second_split(s,"?"))


def third_split(string, delimiter):
	split_string = list()
	prev_split = 0
	for i,s in enumerate(string):
		# traceback.print_stack(file=sys.stdout)
		if s == delimiter:
			split_string.append(string[prev_split:i])
			prev_split = i + 1
	split_string.append(string[prev_split:])
	return split_string

s = "hello how are you?"

print()
print(third_split(s,' '))
print(third_split(s, 'h'))
print(third_split(s, 's'))
print(third_split(s,"?"))