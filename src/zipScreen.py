import shutil
import os

def zipScreenshot():

	get_dir = os.getcwd() + '\data\screenshot' + os.sep

	output_filename = os.getcwd() + '\data\ZipScreenshot'

	if(shutil.make_archive(output_filename, 'zip', get_dir)):
		print True