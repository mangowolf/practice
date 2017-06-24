"""QUESTION 5
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. 
The function definition should look like question5(ll, m), where ll is the first node of a linked list and 
m is the "mth number from the end". You should copy/paste the Node class below to use as a representation of a 
node in the linked list. Return the value of the node at that position.
"""

#Definition for Node class to instantiate node object
class Node(object):
    ##Defines attributes of the object
	def __init__(self,data):
		self.data = data
		self.next = None

#Helper function to generate nodes based on argument number
def generateNode(num):
    ##Creates nodes up to the number provided

    nodeArray = {}
    for x in xrange(1,num+1):
        e = Node(x)
        nodeArray[x] = e
    return nodeArray

#Defines a Linked List class
class LinkedList(object):
    ##Defines attributes for the class, in this case defining the head attribute as None.
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def getPosition(self,position):
        """Get a node from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if type(position) != int:
            return "Error: Only non-negative integers accepted"
        current = self.head
        cPosition = 1
        if self.head and position > 0:
            while current:
                if cPosition != position:
                    current = current.next
                    cPosition = cPosition + 1
                else:
                    return current
            return None
        else:
            return None

    def LinkedListLength(self):
        """Get the length of a given linked list"""
        current = self.head
        ll_length = 0
        if self.head:
            while current:
                ll_length = ll_length + 1
                current = current.next
            return ll_length
        else:
            return None

    def question5(self,ll,m):
        length = self.LinkedListLength()
        position = length - m + 1
        return self.getPosition(position).data

nArray = generateNode(5)
LinkedListObj = LinkedList(nArray[1])
LinkedListObj.append(nArray[2])
LinkedListObj.append(nArray[3])
LinkedListObj.append(nArray[4])
LinkedListObj.append(nArray[5])

print LinkedListObj.question5(nArray[1],3)
