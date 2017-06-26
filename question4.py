
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

	def search(self,find_val):
		return self.search_helper(self.root,find_val)

	def search_helper(self,current,find_val):
		if find_val == current.value:
			return current.value
		elif find_val < current.value:
			if current.value:
				current = current.left
				return self.search_helper(current,find_val)
			else:
				return False
		elif find_val > current.value:
			if current.value:
				current = current.right
				return self.search_helper(current,find_val)
			else:
				return False

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

	tree = createBST(T,r).root
	def lca(root,n1,n2):

		#Base Case
		if root is None:
			return None

		if(root.value > n1 and root.value >n2):
			return lca(root.left, n1, n2)

		if(root.value < n1 and root.value < n2):
			return lca(root.right, n1, n2)

		return root

	t = lca(tree,n1,n2)
	return t.value

print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

"""
#Initialize Tree
tree = BST(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

#Test search
print tree.search(4)
print tree.search(3)"""