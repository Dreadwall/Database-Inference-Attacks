import re
from itertools import islice

INPUT_LOC = "/Users/frank/Documents/cmu-17-18/15-421/nulled_io/nulled_io.txt"
OUTPUT_LOC = "/Users/frank/Documents/cmu-17-18/15-421/nulled_io"

def parse_tablename(s):
	cs = []
	build = False
	for c in s:
		if c == '`' and not build:
			build = True
		elif (c == '`' or c == '?') and build:
			return "".join(cs)
		elif build:
			cs.append(c)

def write_table(lines, outfile):
	table = "".join(lines)
	build = False
	parCount = 0

	for char in table:
		if char == "(":
			parCount += 1
			if parCount == 1:
				entry = []
				build = True
		elif char == ")":
			parCount -= 1
			if parCount == 0:
				outfile.write("".join(entry)+"\n")
				build = False
		if build:
			if not(char == "(" and parCount == 1):
				entry.append(char)

def clean_nulledio():
	infile = open(INPUT_LOC, "r", encoding='latin-1')
	STRUCTURE_RE = r"^-- Table structure for table `.+`"
	DUMP_RE = r"^-- Dumping data for table `.+`"

	outfile = None
	tablename = None
	tablelines = []
	mode = None

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
			# if structure then new file
			if re.match(STRUCTURE_RE, line):
				# write data and close old output file
				if outfile:
					write_table(tablelines, outfile)
					outfile.close()

				mode = "structure"
				tablename = parse_tablename(line)
				tablelines = []
				outfile_loc = OUTPUT_LOC + "/" + tablename + ".txt"
				outfile = open(outfile_loc, 'w')
				outfile.write("--\n" + line)

			# if dump then switch mode
			elif re.match(DUMP_RE, line):
				if parse_tablename(line) == tablename:
					mode = "dump"
					outfile.write(line + "--\n\n")

			# else write the line
			else:
				if mode == "structure" and outfile:
					outfile.write(line)
				elif mode == "dump" and outfile:
					tablelines.append(line)

	infile.close()

clean_nulledio()
