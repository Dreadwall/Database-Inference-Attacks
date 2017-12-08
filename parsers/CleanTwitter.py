import re
from itertools import islice

INPUT_LOC = ""
OUTPUT_LOC = ""

def clean_twitter():
	infile = open(INPUT_LOC, "r", encoding='latin-1')
	outfile = open(OUTPUT_LOC, "w")

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
			items = line.split(":", 1)
			if len(items) != 2:
				continue

			# EMAIL:PASSWORD
			# clean login
			if re.match(r"^@.*", items[0]):
				items[0] = items[0][1:]

			items[0] = items[0].replace("ã", '')
			items[0] = items[0].replace("â", '')
			items[0] = items[0].replace("¢", '')
			items[0] = items[0].replace("¬", '')


			# check login validiity
			isEmailRe = r".+@.+"
			emailRe = r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
			usernameRe = r"^@?[A-Za-z0-9\.\+_-]+$"
			if re.match(isEmailRe, items[0]) and not re.match(emailRe, items[0]):
				print("Bad email: " + items[0])
				items[0] = "NULL"
			elif not re.match(isEmailRe, items[0]) and not re.match(usernameRe, items[0]):
				print("Bad username: " + items[0])
				items[0] = "NULL"

			for i in range(2):
				if items[i] == "":
					print("Blank attr: " + str(i))
					items[i] = "NULL"

			if items[0] == "NULL":
				continue

			# write
			outfile.write(":".join(items))

	infile.close()
	outfile.close()

clean_twitter()