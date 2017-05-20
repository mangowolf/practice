list = ['banana', 'apple', 'cherry']
def listGen(list):
	string = ""
	for item in list:
		string += "<ul>" + str(item) + "<ul>"
	return string

print listGen(list)

print "Hello World!"

def foo(y):
	def bar(x):
		return x + y
	return bar

b = foo(1)
print b(2)