
class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST(object):
	def __init__(self, root):
		self.root = Node(root)

	def insert(self, new_val):
		return self.insert_helper(self.root, new_val)

	def insert_helper(self, current, new_val):
		if new_val < current.value:
			if current.left == None:
				current.left = Node(new_val)
			else:
				current = current.left
				return self.insert_helper(current, new_val)
		elif new_val > current.value:
			if current.right == None:
				current.right = Node(new_val)
			else:
				current = current.right
				return self.insert_helper(current, new_val)

#Create the Binary search tree based on a given matrix and identified root value
def createBST(T, r):
	matrix = T
	length = len(matrix)
	bst = BST(r)
	for r in xrange(0,length):
		innerLength = len(matrix[r])
		for c in xrange(0, innerLength):
			if matrix[r][c] == 1:
				bst.insert(c)
	return bst

def question4(T,r,n1,n2):

	parent = createBST(T,r).root
	def lca(root,n1,n2):

		#Base Case
		if root is None:
			return None

		"""Check if the the parent root value is greater than both children,
		if so, recursively check until the base case is found"""
		if(root.value > n1 and root.value >n2):
			return lca(root.left, n1, n2)

		"""Check if the parent root value is less than both children,
		if so, recursively check until the base case is found"""
		if(root.value < n1 and root.value < n2):
			return lca(root.right, n1, n2)

		"""When the common ancestor is found, return the root value."""
		return root

	commonAncestor = lca(parent,n1,n2)
	return commonAncestor.value

print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)