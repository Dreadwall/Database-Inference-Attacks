from hashlib import sha256
from os import remove

def hasher(string):
	return sha256(bytes(string, encoding="utf-8")).hexdigest()

file_input = "Data/MySpace_Clean.txt"
file_output = "Hashed/MySpace_Hashed.txt"
#columns for Atlanta FBI = [0,3]
#columns for Web Host = [1=email]
#columns for XFactor = [5=email] 
#columns for Twitter = [0=email]
#columns for MySpace = [1=email]
columnsToHash = [1]

x = 0
y = 1

try:
    remove(file_output)
except OSError:
    pass

new_file = open(file_output, "a", encoding="utf-8")
with open(file_input, "r", encoding="utf-8") as f:
	line = f.readline()
	while line != '':
		x += 1
		columns = line.split(':')
		for i in range(len(columns)):
			if i in columnsToHash:
				new_file.write(hasher(columns[i]))
			else: 
				new_file.write(columns[i])
			if (i < (len(columns)-1)):
				new_file.write(":")
		if x == 1000:
			new_file.close()
			new_file = open(file_output, "a", encoding="utf-8")
			x = 0
			y += 1000
			print(y)
		line = f.readline()
	new_file.close()