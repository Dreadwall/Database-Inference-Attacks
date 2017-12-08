import re
from itertools import islice

INPUT_LOC = "000webhost.com.txt"
OUTPUT_LOC = "cleanedWebHost.txt"

def clean_twitter():
	infile = open(INPUT_LOC, "r", encoding='latin-1')
	outfile = open(OUTPUT_LOC, "w", encoding='latin-1')

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
			# print(line)
			items = line.split(":", 3)
			if len(items) != 4:
				continue
			# print(items)
			# USERNAME:EMAIL:IP:PASSWORD
			# clean login
			if re.match(r"^@.*", items[0]):
				items[0] = items[0][1:]
			if re.match(r"^[\ ,-,\.]*$", items[0]):
				items[0] = "NULL"

			# check login validiity
			isEmailRe = r".+@.+"
			emailRe = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
			usernameRe = r"^@?[A-Za-z0-9\.\+_-]+$"
			if re.match(isEmailRe, items[1]) and not re.match(emailRe, items[1]):
				# print("Bad email: " + items[1])
				items[1] = "NULL"
			elif not re.match(isEmailRe, items[1]) and not re.match(usernameRe, items[1]):
				# print("Bad username: " + items[1])
				items[1] = "NULL"

			for i in range(0,3):
				if items[i] == "":
					# print("Blank attr: " + str(i))
					items[i] = "NULL"

			if items[2] == "NULL":
				continue

			# write
			try:
				outfile.write(":".join(items))
			except:
				print("Error")

	infile.close()
	outfile.close()

clean_twitter()