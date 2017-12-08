import re
from itertools import islice

DETAILS_LOC = "/Users/frank/Documents/cmu-17-18/15-421/ALM/new/member_details.txt"
LOGIN_LOC = "/Users/frank/Documents/cmu-17-18/15-421/ALM/new/member_login.txt"
OUTPUT_LOC = "/Users/frank/Documents/cmu-17-18/15-421/ALM/new/members.txt"

def read_member_file(file, fields, wanted_fields):
	logins = dict()
	while True:
		head = list(islice(file, 61*3))
		if not head:
			print('EOF')
			break
		for line in head:
			items = line.split("||")
			if len(items) == fields:
				pnum = items[0]
				wanted_items = []
				for index in wanted_fields:
					wanted_items.append(items[index])
				logins[pnum] = wanted_items
			else:
				print(items)
	return logins

def main():
	details_file = open(DETAILS_LOC, "r")
	login_file = open(LOGIN_LOC, "r")
	outfile = open(OUTPUT_LOC, "w")

	wanted_items = [3, 5, 6, 7, 9, 10]
	details = read_member_file(details_file, 12, wanted_items)
	details_file.close()

	wanted_fields = [1, 2]
	print("finished details")
	while True:
		head = list(islice(login_file, 61*3))
		if not head:
			print('EOF')
			break

		for line in head:
			items = line.split("||")
			if len(items) == 5:
				pnum = items[0]
				if pnum in details:
					other_items = details[pnum]
					items = [items[1], items[2]] + other_items
				else:
					items = [items[1], items[2]] + ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
				outfile.write("||".join(items) + "\n")
			else:
				print("logins not 5")

	login_file.close()
	outfile.close()
main()