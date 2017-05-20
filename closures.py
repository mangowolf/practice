def foo(y):
	def bar(x):
		return x + y
	return bar

b = foo(1)
print b(2)
