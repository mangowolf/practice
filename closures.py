def wrapper(y):
	def closure(x):
		return x + y
	return closure

obj = wrapper(1)
print obj(2)
print obj(3)