import re
from itertools import islice

INPUT_LOC = "/Users/Alex/Desktop/Carnegie/15-421/Datasets/Myspace.com.txt"
OUTPUT_LOC = "/Users/Alex/Desktop/TestOut.txt"


def clean_Myspace():

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
			temp = item.split(":",5)
			if(len(temp) != 5):
				continue
			#id : email : id/username : sha1(strtolower(substr($pass, 0, 9))) : sha1($id . $pass)
			if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",temp[1]):
				temp[1] = "NULL"
			for x in range(2,5):
				if(temp[x] == ""):
					temp[x] = "NULL"

			if(temp[1] == "NULL" and (temp[2] == temp[0]) or temp[2] == "NULL"):
				continue

			f2.write(temp[0] + ":" +  temp[1] + ":" +  temp[2] + ":" +  temp[3] + ":" +  temp[4])


	myfile.close()
	f2.close()