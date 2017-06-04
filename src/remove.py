import os
import glob

def remove_screenshot():
	directory = os.getcwd() + '\\data\\screenshot\\'
	#directory_test='..\\data\\screenshot\\'
	os.chdir(directory)
	files=glob.glob('*.png')
	for filename in files:
	    os.unlink(filename)


def remove_ZipScreenshot():
	direct = os.getcwd() + os.sep + 'data\\ZipScreenshot.zip'

	os.remove(direct)