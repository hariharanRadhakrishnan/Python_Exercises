"""
def func_name():
    ''' Function implementation'''

func_name = (decorator(params))(func_name)
"""

def decorator(*args, **kwargs):
    print("Inside decorator")
    def inner(func):
        print("Inside inner function")
        print("I like", kwargs['like'])
        return func 
    return inner

@decorator(like = "geeksforgeeks")
def func():
    print("Inside actual function")

func()
func()


def decorator(str):
    print(str)
    def inner(func):
        print("Inside inner function")
        return func 
    return inner

@decorator("geeksforgeeks")
def func():
    print("Inside actual function")


func()
func()

def divide_by_2(str):
	print(str)
	def wrap_inner(func):
		# print(func.__name__)
		def inner(a,b):
			# print("Inside inner function")
			return func(a,b)/2
		return inner
	return wrap_inner

@divide_by_2("Get output of add divided by 2")
def add(a,b):
    return a+b

@divide_by_2("Get output of mul divided by 2")
def mul(a,b):
	return a*b

print(add(1,2))
print(add(2,3))
print(add(2,2))

print(mul(2,4))
print(mul(9,3))
print(mul(5,5))


keyword_dict = dict()

def keyword(str):
	global keyword_dict
	def inner(func):
		keyword_dict[str] = func.__name__
		return func
	return inner

@keyword('load topology "${file_name}"')
def load_topology(top_file_name):
	print("loading {0}".format(top_file_name))

print("\n\n")
load_topology("topology.yaml")

print("\n",keyword_dict)

def run_robot_keyword(key_str):
	pass #question