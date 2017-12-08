import re
from itertools import islice

INPUT_LOC = "/Users/frank/Documents/cmu-17-18/15-421/nulled_io/members.txt"
OUTPUT_LOC = "/Users/frank/Documents/cmu-17-18/15-421/nulled_io/new/users.txt"

def read_line(line):
	seen_sep = False
	sep_prev = False
	items = []
	item = []

	for ch in line:
		if ch == "'":
			item.append(ch)
			seen_sep = True
			sep_prev = True
		elif (ch == "," or ch == "\n") and ((not seen_sep) or (seen_sep and sep_prev)):
			items.append("".join(item))
			sep_prev = False
			seen_sep = False
			item = []
		else:
			item.append(ch)
			sep_prev = False

	return items

def read_mess(mess):
	good = []
	index = 0
	ends = set()
	while(index < len(mess)):
		item = mess[index]
		if "(" in item:
			mess[index] = read_member_id(item)
			ends.add(index + 98)
		elif ")" in item:
			if index in ends:
				beginning = index - 98
				end = index + 1
				good.append(mess[beginning:end])
		index = index + 1
	return good

def read_member_id(s):
	mem_id = []
	for ch in s[::-1]:
		if ch == "(":
			mem_id.reverse()
			return "".join(mem_id)
		else:
			mem_id.append(ch)

def clean_nulledio_members():
	infile = open(INPUT_LOC, "r")
	outfile = open(OUTPUT_LOC, "w")
	reqs = [
		'\n',
		'--\n',
		'-- Dumping data for table `members`\n'
	]
	item_indices = [0, 1, 3, 5, 18, 19, 20, 43, 44, 48, 49, 53, 54, 59, 63]
	line_count = 0
	new_line_count = 0
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
			line_count = line_count + 1
			if len(reqs) > 0 and line == reqs[-1]:
				reqs.pop()
			else:
				items = read_line(line)
				if len(items) == 99:
					new_line_count = new_line_count + len(items) // 99
					items_w = [items[i] for i in item_indices]
					outfile.write("|".join(items_w) + "\n")
				elif len(items) > 99:
					for new_items in read_mess(items):
						if (len(new_items) != 99):
							print("read_mess wrong")
						new_line_count = new_line_count + 1
						items_w = [new_items[i] for i in item_indices]
						outfile.write("|".join(items_w) + "\n")

	print(line_count, new_line_count)
	infile.close()
	outfile.close()

clean_nulledio_members()
