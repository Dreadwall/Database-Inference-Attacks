files_list = [#["Hashed/Atlanta_FBI_Hashed.txt", 0, "Atlanta FBI"], 
			  #["Hashed/MySpace_Hashed.txt", 1, "MySpace"],
			  ["Hashed/MySpace/MySpace_Part_6.txt", 2, "MySpace"],
			  #["Hashed/Twitter_Hashed.txt", 0, "Twitter"],
			  #["Hashed/Web_Host_Hashed.txt", 1, "Web Host"], # For Email
			  #["Hashed/Web_Host_Hashed.txt", 0], # For Username
			  #["Hashed/XFactor_Hashed.txt", 5, "XFactor"],
			  ["Hashed/Ashley_Madison_Hashed.txt", 0, "Ashley Madison"],
			  #["Hashed/Nulled_IO_Hashed.txt", 2, "Nulled.io"] # For Email
			  #["Hashed/Nulled_IO_Hashed.txt", 1, "Nulled.io"] # For Username
			 ]

total_records = [0,0]
data_hash = dict()

for file_index in range(len(files_list)):
	file = files_list[file_index]
	current_hash = dict()
	with open(file[0], encoding='utf-8') as f:
		current_line = f.readline()
		while current_line != '':
			identifier = current_line.split(":")[file[1]]
			if identifier in data_hash:
				data_hash[identifier] += 1
			else:
				current_hash[identifier] = 0
			current_line = f.readline()
			total_records[file_index] += 1
		data_hash.update(current_hash)
		f.close()

total = 0
for key in data_hash:
	if data_hash[key] > 0:
		total += data_hash[key]

print(total_records)
print(total)
