from itertools import islice
from hashlib import sha256

def hash_string(string):
	return sha256(bytes(string, encoding="utf-8")).hexdigest()

# inserts file into a hash (outer join)
def file_into_hash(file, formatter, hashh=dict()):
	line_count = 0
	while True:
		head = list(islice(file, 61*3))
		if not head:
			break
		for line in head:
			line_count = line_count + 1
			items, key = formatter(line)
			if not key:
				pass
			elif key in hashh:
				new_line = "||".join(items)
				hashh[key].append(new_line)
			else:
				new_line = "||".join(items)
				hashh[key] = [new_line]
	print('file_into_hash ', line_count)
	return hashh

# inner joins file with a hash
def file_with_hash(hashh, file, formatter):
	line_count = 0
	new_hashh = dict()
	while True:
		head = list(islice(file, 61*3))
		if not head:
			break
		for line in head:
			line_count = line_count + 1
			items, key = formatter(line)
			if not key:
				pass		
			elif key in new_hashh:
				new_line = "||".join(items)
				new_hashh[key].append(new_line)
			elif key in hashh:
				new_line = "||".join(items)
				new_hashh[key] = hashh[key] + [new_line]
				hashh.pop(key, None)
	print('file_with_hash', line_count)
	return new_hashh

def write_hash(hashh, file):
	for key in hashh:
		lines = hashh[key]
		if len(lines) < 2:
			print(lines)
		else:
			for line in lines:
				file.write(line + "\n")

# DEFINE FORMATTERS HERE
# param - line:String
# returns attrs:[String] of size 22, corresponding to the defined online profile attributes
# returns key:String, the string to match in other files
#
# * use blank string in output array if attribute isn't in line
# * hash attributes when appropriate
def am_formatter(line):
	items = line.split("||")
	if len(items) != 8:
		print("wrong #", line)
		return None, None
	output = [''] * 22
	output[7] = '' if items[0] == 'NULL' else hash_string(items[0])
	output[8] = '' if items[1] == 'NULL' else items[1]
	output[4] = '' if items[2] == 'NULL' else items[2]
	output[2] = '' if items[3] == 'NULL' else items[3]
	return output, items[0]
def ms_formatter(line):
	items = line.split(":")
	if len(items) != 5:
		print("wrong #", line)
		return None, None
	output = [''] * 22
	output[5] = '' if items[1] == 'NULL' else hash_string(items[1])
	output[7] = '' if items[2] == 'NULL' else hash_string(items[2])
	output[8] = '' if items[3] == 'NULL' else items[3]
	return output, items[2]

# main function
def main():
	# file_into_hash(smaller files) and then file_with_hash(larger files)
	DIR = 'C:\\Users\\suadmin\\Documents\\school\\cmu-17-18\\15-421\\'

	OUTPUT = open(DIR + 'am_ms.txt', 'w')
	SMALL_FILE = open(DIR + 'users.txt', 'r', encoding="utf-8")
	LARGE_FILE = open(DIR + 'MySpace_Clean.txt', 'r')

	hashh = file_into_hash(SMALL_FILE, am_formatter)
	hashh = file_with_hash(hashh, LARGE_FILE, ms_formatter)

	write_hash(hashh, OUTPUT)

	OUTPUT.close()
	SMALL_FILE.close()
	LARGE_FILE.close()

main()