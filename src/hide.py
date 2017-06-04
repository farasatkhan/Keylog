import ctypes
import os


def hide_screenshot():
	FILE_ATTRIBUTE_HIDDEN = 0x02
	get_dir = os.getcwd() + '\\data\\screenshot'
	ret = ctypes.windll.kernel32.SetFileAttributesW(get_dir, FILE_ATTRIBUTE_HIDDEN)

	if ret:
	    print 'attribute set to Hidden'
	else:  # return code of zero indicates failure, raise Windows error
	    raise ctypes.WinError()