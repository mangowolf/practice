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

"""print question('udacity', 'ad')
print question('1up2', 21)
print question('\delete', 't\ele')
print question('Nordic', 'Ndd')
print question('Nordic', 'ndd')
print question('Nordic', 'Nd')
print question('Nordic', 'nd')
"""

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


print question2('redivider')
#should print out redivider
print question2('forgeeksskeegfor')
#should print out geeksskeeg