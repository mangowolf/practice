def bigSmall(array,n):
	big = array[0]
	small = array[0]
	arrLength = len(array)
	for i in xrange(0,arrLength):
		if small > array[i]:
			small = array[i]
		if big < array[i]:
			big = array[i]

	return big,small

array = [5,15,23,17,0,46,-1,7]
print bigSmall(array,0)

def checkFormat(braces):
	s = []
	balanced = True
	index = 0

	braceStringLength = len(braces)
	while index < braceStringLength and balanced:
		symbol = braces[index]
		if symbol == '(':
			s.append('(')
		elif symbol == '[':
			s.append('[')
		elif symbol == '{':
			s.append('{')
		else:
			if not s:
				return False
			else:
				s.pop()

		index = index + 1

	if balanced and not s:
		return True
	else:
		return False

braces = '()[]'
braces1 = '[()]'
braces2 = ')([]'
braces3 = '{[}]'
print checkFormat(braces)
print checkFormat(braces1)
print checkFormat(braces2)
print checkFormat(braces3)

def test_balanced_parantheses(string_to_check):

if len(string_to_check) % 2 != 0:

return False

pairs = {

"}": "{",

"]": "[",

")": "(",

}

openers = []

for s in string_to_check:

if s in pairs.values():

openers.append(s)

elif not pairs.has_key(s):

return False #not valid char

elif pairs[s] == openers[-1]:

openers.pop()

return len(openers) == 0