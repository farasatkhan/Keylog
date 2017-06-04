import os
import sys

def create_screenshot():
	if not os.path.exists('screenshot'):
		os.makedirs('screenshot')
	else:
		return

# create data directory
def create_directory(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
		create_file(directory)
	else:
		return

# create a file called keystrokes at data/keystrokes.txt
def create_file(filename):
	f = filename + '/keystrokes.txt'
	if not os.path.isfile(f):
		write_file(f, 'Text conatining file')
	else:
		return

# write to file
def write_file(file, text):
	try:
		f = open(file, 'w')
		f.write(text)
		f.close()
	except OSError as e:
		pass

def delete_content(file):
	with open(file, 'w') as f:
		pass


# append to keystroke file
def append_file(file, text):
	with open(file, 'a') as f:
		f.write(text)
		f.close()