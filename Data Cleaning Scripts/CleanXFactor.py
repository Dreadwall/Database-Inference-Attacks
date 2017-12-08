import re
from itertools import islice

INPUT_LOC = "/Users/Alex/Desktop/Carnegie/15-421/Datasets/xfactor-database.txt"
OUTPUT_LOC = "/Users/Alex/Desktop/TestOut.txt"


def clean_Xfactor():
	#I removed every line before 10 | Nathan ... before running this

	myfile =  open(INPUT_LOC, "r")
	f2 = open(OUTPUT_LOC, "w")
	while True:
		#Pythons internal buffer is 4k
		#Lets assume average of 65 char lines
		#61 lines pulled in per read
		#Guess 3 pages given to python
		head = list(islice(myfile, 61*3))
		if not head:
			break


		for item in head:
			temp = item.split(" | ",14)
			if(len(temp) != 14):
				continue
			#id | firstname | lastname | dob | phone | email | auditiontype | numberofperformers | location | optin_1 | optin_2 | gender | zip | timestamp
			if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",temp[5]):
				temp[5] = "NULL"
			for x in range(1,14):
				if(temp[x] == "" or temp[x] == "0"):
					temp[x] = "NULL"

			if(temp[1] == "NULL" and temp[2] == "NULL" and temp[5] == "NULL"):
				continue

			final = ""
			for x in range(0,13):
				final = final + temp[x] + ":"
			final = final + temp[13]
			f2.write(final)


	myfile.close()
	f2.close()