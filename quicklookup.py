#!/usr/local/bin/python3

filename = input("Please enter name of data file: ")

file = open(filename, "r")
lines = file.readlines()
file.close()

words = {}
linenum = 1

for line in lines :
	listofwords = line.split()
	for word in listofwords :
		word = word.lower()
		word = word.strip(".,!?'\"")
		
		if word in words :
			words[word].add(linenum)
		else :
			words[word] = {linenum}

	linenum += 1

again = 'y'

while again == 'y' :
	query = input("Please enter a group of words to search for: ")

	listofwords = query.split()

	if len(listofwords) == 0 :
		answerset = set()
	else :
		answerset = words.get(listofwords[0].lower(),set())

		for word in listofwords[1:] :
			answerset = answerset & words.get(word.lower(),set())

	print(sorted(list(answerset)))

	again = input("Do you want to do it again? ")

