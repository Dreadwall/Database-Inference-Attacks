file = "Hashed/MySpace_Hashed.txt"

file_number = 1
file_name = "Hashed/MySpace/MySpace_Part_"
new_file = open(file_name + str(file_number), "a", encoding="utf-8")

with open(file, "r", encoding="utf-8") as f:
	records_count = 0
	current_line = f.readline()
	while current_line != '':
		current_line = f.readline()
		records_count += 1
		new_file.write(current_line)
		if records_count % 30000000 == 0:
			file_number += 1
			new_file.close()
			new_file = open(file_name + str(file_number), "a", encoding="utf-8")
			print("On file #" + str(file_number))

print("Done")
