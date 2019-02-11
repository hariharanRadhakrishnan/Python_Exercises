def normal_decorator(function):
	def inner(str):
		print("before function")
		function(str)
		print("after function")
		return function
	return inner

@normal_decorator
def print_str(str):
	print(str)

new_f = print_str("hello")
print_str("world")
new_f("whats up")

def decorator2(function):
	def inner():
		print("before function")
		function(str)
		print("after function")
	return inner

@decorator2
def print_str(str):
	print(str)

# print_str("hello") #error: saying parameter given