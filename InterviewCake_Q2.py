'''InterviewCake_q2'''

array = [1,7,3,4]

#Efficiency is O(n^2) and space is O(n)
def get_products_of_all_ints_except_at_index(array):

	product = []
	n = len(array)
	'''
	for i in xrange(0,n):
		value = 1
		for j in xrange(i,n):
			if i == j:
				continue
			value = value * array[j]
		product.append(value)
	'''
	value = 1
	for i in xrange(0,n):
		value = value * array[i]
	product.append(value)
	return product

print get_products_of_all_ints_except_at_index(array)