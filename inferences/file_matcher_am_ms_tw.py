from itertools import islice
from hashlib import sha256

def hash_string(string):
	return sha256(bytes(string, encoding="utf-8")).hexdigest()

# inserts file into a hash (outer join)
def outer_join_hash(file, formatter, hashh=dict()):
	line_count = 0
	while True:
		head = list(islice(file, 61*3))
		if not head:
			break
		for line in head:
			line_count = line_count + 1
			items, key = formatter(line)
			if key is None:
				pass
			elif key in hashh:
				new_line = "||".join(items)
				hashh[key].append(new_line)
			else:
				new_line = "||".join(items)
				hashh[key] = [new_line]
	print('outer_join_hash ', line_count)
	return hashh

def left_join_hash(hashh, file, formatter):
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
	print('left_join_hash ', line_count)
	return hashh

# inner joins file with a hash
def inner_join_hash(hashh, file, formatter):
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
		for line in lines:
			if line[len(line) - 1] == '\n':
				file.write(line)
			else: 
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
def tw_formatter(line):
	i = line.find(':')
	items = [line[0:i], line[i + 1:]]
	if len(items) != 2:
		print('wrong #', line)
		return None, None
	output = [''] * 22
	if '@' in items[0]:
		output[5] = hash_string(items[0])
		output[8] = hash_string(items[1])
		return output, output[5]
	else:
		output[7] = hash_string(items[0])
		output[8] = hash_string(items[1])
		return None, None
def combined_formatter(line):
	items = line.split('||')
	if len(items) != 22:
		print('wrong #', line)
		return None, None
	return items, items[5]

# main function
def main():
	# file_into_hash(smaller files) and then file_with_hash(larger files)
	DIR = 'C:\\Users\\suadmin\\Documents\\school\\cmu-17-18\\15-421\\'

	OUTPUT = open(DIR + 'am_ms_tu_te.txt', 'w')
	SMALL_FILE = open(DIR + 'am_ms_tu.txt', 'r', encoding="utf-8")
	LARGE_FILE = open(DIR + 'Twiter_Clean.txt', 'r', encoding="utf-8")

	hashh = outer_join_hash(SMALL_FILE, combined_formatter)
	hashh = left_join_hash(hashh, LARGE_FILE, tw_formatter)

	write_hash(hashh, OUTPUT)

	OUTPUT.close()
	SMALL_FILE.close()
	LARGE_FILE.close()

main()