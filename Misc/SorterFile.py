file_name = "Hashed/XFactor_Hashed.txt"
new_file_name = "Sorted/XFactor_Sorted.txt"
comparisonIndex = 5

def compare(a, b):
	return a and b and a.split(":")[comparisonIndex] < b.split(":")[comparisonIndex]

def insertionSort():
	linesSeen = set()
	linesInNewFile = 0
	totalLines = 0
	firstPass = True
	with open(new_file_name, "a", encoding="utf-8") as new_file:
		while linesInNewFile != totalLines or firstPass:
			data = open(file_name, "r", encoding="utf-8")
			currentLine = data.readline()
			lowestAlphabeticalLine = currentLine
			currentLineNumber = 0
			lowestLineNumber = 0
			while (currentLineNumber in linesSeen and currentLine != ''):
				lowestLineNumber = currentLineNumber
				lowestAlphabeticalLine = currentLine
				currentLine = data.readline()
				currentLineNumber += 1
			while currentLine != '':
				if firstPass:
					totalLines += 1
				if currentLineNumber not in linesSeen:
					if compare(currentLine, lowestAlphabeticalLine):
						lowestAlphabeticalLine = currentLine
						lowestLineNumber = currentLineNumber
				currentLine = data.readline()
				currentLineNumber += 1
			new_file.write(lowestAlphabeticalLine)
			linesSeen.add(lowestLineNumber)
			linesInNewFile += 1
			data.close()
			firstPass = False

insertionSort()
