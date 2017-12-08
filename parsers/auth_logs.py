import re
from itertools import islice

INPUT_LOC = "/Users/frank/Documents/cmu-17-18/15-421/nulled_io/auth_logs.txt"
OUTPUT_LOC = "/Users/frank/Documents/cmu-17-18/15-421/nulled_io/new/auth_logs.txt"

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

def clean_nulledio_auth_logs():
	infile = open(INPUT_LOC, "r")
	outfile = open(OUTPUT_LOC, "w")
	reqs = [
		'\n',
		'--\n',
		'-- Dumping data for table `auth_logs`\n'
	]

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
			if len(reqs) > 0 and line == reqs[-1]:
				reqs.pop()
			else:
				items = read_line(line)
				if len(items) == 8:
					items_w = [items[1], items[2], items[5]]
					outfile.write("|".join(items_w) + "\n")
			
	infile.close()
	outfile.close()

clean_nulledio_auth_logs()
