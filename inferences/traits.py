from itertools import islice

dir = 'C:\\Users\\suadmin\\Documents\\school\\cmu-17-18\\15-421\\'
# 		if len(line.split('||')) != 22:
# 			print(line) 
# 		login = line.split('||')[7]
# 		# print(login)
# 		if login not in prev_logins:
# 			prev_logins[login] = 1
# 		else:
# 			prev_logins[login] = prev_logins[login] + 1

# for login in prev_logins:
# 	matches = matches + 1
# 	if prev_logins[login] == 1:
# 		print('singleton' + login)

def line_count(path):
	file = open(path, 'r', encoding='utf-8')
	line_count = 0
	while True:
		head = list(islice(file, 61*3))
		if not head:
			print('EOF')
			break
		for line in head:
			if len(line.split('||')) != 22:
				print('Wrong items linecount ', line)
			line_count = line_count + 1
	print('Line count ', line_count)

def email_count(path):
	file = open(path, 'r', encoding='utf-8')
	emails = set()
	email_count = 0
	while True:
		head = list(islice(file, 61*3))
		if not head:
			print('EOF')
			break
		for line in head:
			items = line.split('||')
			if len(items) != 22:
				print('Wrong items email', line)
			elif items[5] == '':
				email_count = email_count + 1
			elif items[5] not in emails:
				emails.add(items[5])
				email_count = email_count + 1
	print('Email_count ', email_count)


def username_count(path):
	file = open(path, 'r', encoding='utf-8')
	usernames = set()
	username_count = 0
	while True:
		head = list(islice(file, 61*3))
		if not head:
			print('EOF')
			break
		for line in head:
			items = line.split('||')
			if len(items) != 22:
				print('Wrong items username', line)
			elif items[7] == '':
				username_count = username_count + 1
			elif items[7] not in usernames:
				usernames.add(items[7])
				username_count = username_count + 1
	print('Username_count ', username_count)

def peek(path, lines = 100):
	file = open(path, 'r', encoding='utf-8')
	line_count = 0
	while line_count < lines:
		head = list(islice(file, 61*3))
		if not head:
			print('EOF')
			break
		print("".join(head))
		line_count = line_count + 1
	
line_count(dir + 'am_ms_tu_te.txt')
username_count(dir + 'am_ms_tu_te.txt')
email_count(dir + 'am_ms_tu_te.txt')
