from hashlib import sha256

def hasher(string):
	return sha256(bytes(string, encoding="utf-8")).hexdigest()

file_input = "Data/MySpace_Clean.txt"
file_output = "Hashed/MySpace_Hashed.txt"
#columns for Atlanta FBI = [0,3]
#columns for Web Host = [1=email]
#columns for XFactor = [5=email] 
#columns for Twitter = [0=email]
#columns for MySpace = []
columnsToHash = [0]

with open(file_input, "r", encoding="utf-8") as f:
	with open(file_output, "w", encoding="utf-8") as new_file:
		for line in f.readlines():
			columns = line.split(':')
			for i in range(len(columns)):
				if i in columnsToHash:
					new_file.write(hasher(columns[i]))
				else: 
					new_file.write(columns[i])
				if (i < (len(columns)-1)):
					new_file.write(":")
		new_file.close()