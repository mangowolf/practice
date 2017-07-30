class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None

class LinkedList(object):
	def __init__(self,head=None):
		self.head = head

class insert(self, new_node):
	current = self.head
	if self.head:
		while current.next:
			current = current.next
		current.next = new_element
	else:
		self.head = new_element