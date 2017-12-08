import re
from itertools import islice

INPUT_LOC = "/Users/Alex/Desktop/Carnegie/15-421/Datasets/Infragard_Atlanta_Users.txt"
OUTPUT_LOC = "/Users/Alex/Desktop/TestOut.txt"


def clean_FBI():

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
			temp = item.split(" | ",4)
			if(len(temp) != 4):
				continue
			#EMAIL | PASS | USERNAME | NAME = CRACKED PASSWORD
			if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",temp[0]):
				temp[0] = "NULL"
			

			for x in range(0,4):
				if(temp[x] == ""):
					temp[x] = "NULL"


			if(temp[0] == "NULL" or temp[2] == "NULL"):
				continue

			f2.write(temp[0] + ":" +  temp[1] + ":" +  temp[2] + ":" +  temp[3].replace(" = ", ":") )


	myfile.close()
	f2.close()