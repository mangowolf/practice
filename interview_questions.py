##############################
######TECHNICAL INTERVIEW QUESTIONS
###QUESTION 1

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

print question('udacity', 'ad')
print question('1up2', 21)
print question('\delete', 't\\ele')
print question('Nordic', 'Ndd')
print question('Nordic', 'ndd')
print question('Nordic', 'Nd')
print question('Nordic', 'nd')



"""
import cgi

def question(s,t):
	lowerS = str.lower(str(cgi.escape(s)))
	lowerT = str.lower(str(cgi.escape(t)))
	letterArray = list(lowerS)
	subLetterArray = list(lowerT)
	wordLetterDict = {i:letterArray.count(i) for i in letterArray}
	subWordLetterDict = {i:subLetterArray.count(i) for i in subLetterArray}
	count = 0
	
	print letterArray
	print subLetterArray
	print wordLetterDict
	print subWordLetterDict
	for subLetter in subLetterArray:
		subValue = subWordLetterDict.get(subLetter)
		if subValue:
			for letter in letterArray:
				value = wordLetterDict.get(letter)
				print subLetter, letter, value, subValue
				if subLetter == letter and value >= subValue:
					count += 1
			print count
	if count == len(subLetterArray):
		return True
	else:
		return False

#print question('udacity', 'ad')
#print question('1up2', 21)
print question('\delete', 'tele')
#print question('Nordic', 'Ndd')
#print question('Nordic', 'ndd')
#print question('Nordic', 'Nd')
#print question('Nordic', 'nd')
"""

"""import cgi

def question(s,t):

	wordArray = list(str(s))
	subWordArray = list(str(t))
	subWordList = {}
	anagram = False
	letCountList = {}
	cnt = 0

	for let in wordArray:
		count = 0
		letCountList[let] = count
		for l in wordArray:
			if let == l:
				count += 1
				letCountList[let] = count

	for swLetter in subWordArray:
		letLeft = letCountList[swLetter]
		print letLeft
		for sLetter in wordArray:
			if swLetter == sLetter and letLeft > 0:
				subWordList[swLetter] = True
				letLeft -= 1
			else:
				subWordList[swLetter] = False

	print subWordList
	for key in subWordList:
		if subWordList[key] == True:
			cnt += 1
	if cnt == len(subWordList):
		return True
	else:
		return False

print question('udacity', 'ad')
print question('1up2', 21)
print question('\delete', 'tele')
print question('Nordic', 'dd')
"""