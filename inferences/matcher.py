from itertools import islice
from hashlib import sha256
DIR_PATH = "/Users/frank/Documents/cmu-17-18/15-421"

def hash_string(string):
	return sha256(bytes(string, encoding="utf-8")).hexdigest()

def dictify_lines(file, field_count, sep=',', login_index=0):
	lines = dict()
	while True:
		head = list(islice(file, 61*3))
		if not head:
			print('EOF')
			break
		for line in head:
			items = line.split(sep)
			if len(items) == field_count:
				# if not lines[items[login_index]]:
				# 	lines[items[login_index]] = ["||".join(items)]
				# else:
				# 	lines[items[login_index]].append("||".join(items))
				if not lines[items[login_index]]:
					lines[items[login_index]] = "||".join(items)
			else:
				print("SMALL: wrong number of items", line)
	return lines

# THIS BE DEFINED SPECIFICALLY FOR EVERY TWO FILES
def combine_items(large_items, small_items):
	li = large_items
	si = small_items
	items = [hash_string(li[1]), hash_string(si[0]), si[1], ]


LARGE_PATH = "/ALM/new/users.txt"
LARGE_SEP = ":"
LARGE_FIELD_COUNT = 4
LARGE_LOGIN_INDEX = 2

SMALL_PATH = "||"
SMALL_SEP = ","
SMALL_FIELD_COUNT = 8
SMALL_LOGIN_INDEX = 0

OUTPUT = "/inferencing/am_ms.txt"
def match():
	file_large = open(DIR_PATH + LARGE_PATH, "r")
	file_small = open(DIR_PATH + SMALL_PATH, "r")
	file_out = open(DIR_PATH + OUTPUT, "w")

	lines_small = dictify_lines(file_small, SMALL_FIELD_COUNT, SMALL_SEP, SMALL_LOGIN_INDEX)
	# find matches
	while True:
		head = list(islice(file_large, 61*3))
		if not head:
			print('EOF')
			break
		for line in head:
			items = line.split(LARGE_SEP)
			if len(items) == LARGE_FIELD_COUNT:
				login = items[LARGE_LOGIN_INDEX]
				if login in lines_small:
					combine(items, lines_small[login].split('||'))
					lines_small.pop(login, "")
			else:
				print("LARGE: wrong number of items", line)
	return logins

match()