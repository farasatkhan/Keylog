from PIL import ImageGrab
import os
import time
import datetime


k = 0
def screen():
    try: 
    	global k

    	location = os.getcwd() + '\data' + os.sep + 'screenshot' + os.sep + 'screenshot_'+ str(k) + '.png'

    	#location_test = '..\\data\\screenshot\\screenshot_'+ str(k) + '.png'

        ImageGrab.grab().save(location)
        k += 1
        
        return True
    except ImportError as e:
        pass
    return False

# x = 0
# while x < 15:
# 	screen()
# 	x += 1