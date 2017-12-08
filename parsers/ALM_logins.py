import re
from itertools import islice

INPUT_LOC = "/Users/frank/Documents/cmu-17-18/15-421/ALM/member_login.txt"
OUTPUT_LOC = "/Users/frank/Documents/cmu-17-18/15-421/ALM/new/member_login.txt"

def read_entry(line):
	in_string_literal = False
	in_string = False
	in_field = False
	in_entry = False

	index = 0
	items = []
	item = []
	while index < len(line):
		ch = line[index]
		if ch == ")" and in_entry and not in_string_literal and not in_string:
			in_entry = False
			items.append("".join(item))
			item = []
		elif ch == "(" and index < 2: 
			in_entry = True
			in_string = False
			in_string_literal = False
			item = []
		elif ch == "(" and line[index - 1] == "," and line[index - 2] == ")":
			in_entry = True
			in_string = False
			in_string_literal = False
			item = []
		elif ch == "," and not in_string_literal and not in_string and in_entry:
			item.append("||")
		elif ch == '"' and not in_string and not in_string_literal:
			in_string = True
		elif ch == '"' and in_string and line[index - 1] != "\\":
			in_string = False
		elif ch == "'" and not in_string_literal and not in_string:
			in_string_literal = True
		elif ch == "'" and not in_string and in_string_literal and line[index - 1] != "\\":
			in_string_literal = False
		elif in_entry:
			item.append(ch)
		index = index + 1
	return items

def seperate_lines():
	infile = open(INPUT_LOC, "r")
	outfile = open(OUTPUT_LOC, "w")
	req = 'INSERT INTO `member_login` VALUES'
	found_req = False
	lines = 0

	while True:
		# Pythons internal buffer is 4k
		# Lets assume average of 65 char lines
		# 61 lines pulled in per read
		# Guess 3 pages given to python
		head = list(islice(infile, 61*3))

		if not head:
			print('EOF')
			break

		for line in head:
			if not found_req and req in line:
				print("found req")
				found_req = True
			if found_req:
				for entry in read_entry(line):
					lines = lines + 1
					if lines % 1000000 == 0:
						print(lines)
					if len(entry.split("||")) != 5:
						print(entry)
					else:
						outfile.write(entry + "\n")
			
	infile.close()
	outfile.close()

seperate_lines()
