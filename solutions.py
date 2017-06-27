##############################
######TECHNICAL INTERVIEW QUESTIONS
###QUESTION 1
"""Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
Your function definition should look like: question1(s, t) and return a boolean True or False."""

import cgi

def question(s,t):
	lowerS = cgi.escape(str.lower(str(s)))
	lowerT = cgi.escape(str.lower(str(t)))
	letterArray = list(lowerS)
	subLetterArray = list(lowerT)
	wordLetterDict = {i:letterArray.count(i) for i in letterArray}
	subWordLetterDict = {i:subLetterArray.count(i) for i in subLetterArray}
	count = 0

	for subLetter in subWordLetterDict:
		subValue = subWordLetterDict.get(subLetter)
		if subValue:
			for letter in wordLetterDict:
				value = wordLetterDict.get(letter)
				if subLetter == letter and value >= subValue:
					count += 1
	if count == len(subWordLetterDict):
		return True
	else:
		return False

#TEST CASES
print question('udacity', 'ad')
print question('1up2', 21)
print question('\delete', 't\ele')
print question('Nordic', 'Ndd')
print question('Nordic', 'ndd')
print question('Nordic', 'Nd')
print question('Nordic', 'nd')

#Efficiency
#O(n^2)


###QUESTION 2
"""Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string."""

#Palindromes: redivider, noon, civic, radar, level, rotor, kayak, reviver, racecar, redder, madam, and refer
import math

def question2(a):
	letterArray = list(a)
	iterations = int(math.ceil(len(a)/2)) + 1
	longPal = []

	if len(a)%2 == 0:
		left = len(a)/2 - 1
		right = left + 1
	elif len(a)%2 > 0:
		left = int(round(len(a)/2,0)) - 1
		right = left + 2
		longPal.append(letterArray[left+1])
		
	for i in range(1,iterations):
		if letterArray[left] == letterArray[right]:
			longPal.insert(0,letterArray[left])
			longPal.append(letterArray[right])
			left -= 1
			right += 1
		else:
			palindrome = "".join(longPal)
			return palindrome

	palindrome = "".join(longPal)
	return palindrome

#TEST CASES
print question2('redivider')
#should print out redivider
print question2('forgeeksskeegfor')
#should print out geeksskeeg

#Efficiency
#O(n)

"""QUESTION 3
Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)"""

parent = dict()
rank = dict()

#Function to make a tree subset
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

#Function to find the root of the path
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

#Function to combine tree subsets
def union(v1, v2):
    r1 = find(v1)
    r2 = find(v2)
    if r1 != r2:
        if rank[r1] > rank[r2]:
            parent[r2] = r1
        else:
            parent[r1] = r2
            if rank[r1] == rank[r2]: 
                rank[r2] += 1

#Function to create the minimum spanning tree using path compression and Kruskals algorithm
def kruskalAlgorithm(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimumSpanningTree = []
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        w, v1, v2 = edge
        if find(v1) != find(v2):
            union(v1,v2)
            minimumSpanningTree.append(edge)

    return minimumSpanningTree

#Function taking in adjacency list graph and returning minimum spanning tree as an adjacency matrix
def question3(G):

    graph = {
        'vertices': G.keys(),
        'edges': []
    }

    for v in G:
        for u in xrange(0,len(G[v])):
            edge = (G[v][u][1],v,G[v][u][0])
            graph['edges'].append(edge)
    
    mst = kruskalAlgorithm(graph)

    adjList = {}
    for i in xrange(0,len(mst)):
        adjList[mst[i][1]] = [mst[i][2],mst[i][0]]

    return adjList

#TEST CASE
G = {'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

print question3(G)

#Efficiency O(n^2)


"""QUESTION 4
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor of both nodes. 
For example, the root is a common ancestor of all nodes on the tree, but if both nodes are descendents 
of the root's left child, then that left child might be the lowest common ancestor. You can assume that 
both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition 
should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index 
of the list is equal to the integer stored in that node and a 1 represents a child node, r is a 
non-negative integer representing the root, and n1and n2 are non-negative integers representing the 
two nodes in no particular order. For example, one test case might be
question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
"""

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

#TEST CASE
print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)

#Efficiency O(n) + O(log n)

#QUESTION 5
"""Find the element in a singly linked list that's m elements from the end. 
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

#TEST CASE
print LinkedListObj.question5(nArray[1],3)

"""Efficiency of question5() is:
	LinkedListLength() is O(n) + self.getPosition() is O(n) = O(2n) which is approximately O(n)
 """