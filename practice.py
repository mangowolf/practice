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

"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
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
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if position < 1:
            return None
        current = self.head
        for i in range(1,position+1):
            if i == position:
                return current
            current = current.next
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position < 1:
            return None
        current = self.head
        for i in range(1,position):
            if i + 1 == position:
                new_element.next = self.get_position(position)
                current.next = new_element
            current = current.next
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous == None:
                    self.head = current.next
                else:
                    previous.next = current.next.next
            previous = current
            current = current.next
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value

"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
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

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        current = self.head
        print current
        self.head = new_element
        print self.head
        new_element.next = current
        print new_element.next

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        if self.head:
            current = self.head
            self.head = current.next
            previous = current
            previous.next = None
            current = self.head
            return previous
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.append(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print stack.pop().value
print stack.pop().value
print stack.pop().value
print stack.pop()
stack.push(e4)
print stack.pop().value

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    half = len(input_array)/2
    while value > input_array[half]:
        half += half/2
        if input_array[half] == value:
            return half
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

"""Recursion practice with the Fibonacci sequence."""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

"""Quick Sort Practice"""
"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    pivot = array[-1]
    n = len(array)
    i = n - 2
    def compare(pivot,n, i):
        while(pivot < array[0]):
            array[n-1] = array[0]
            print array
            array[0] = array[n-2]
            print array
            array[n-2] = pivot
            print pivot
            print i
            i -= 1
            n -= 1
        pivot = array[i-1]
        print array
        return compare(pivot,n,i)
    return compare(pivot,n,i)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)

#Practice with dictionaries
"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print locations
"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order."""

for key in sorted(locations.iterkeys()):
    print "%s: %s" % (key, locations[key])
"""2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""