"""
1   User - choose patient & load a "retina" volume

    (Automated:)
2   Ask user to input patient name/patient ID
3   close QuickVue
4   uncheck "Show Lines"
5   select "Retina"
6   take screenshot 1
7   select "Measure\Density"
8   check "Show Lines"
9   take screenshot 2
10   uncheck "Show Lines"
11  take screenshot 3
12  select "Deep"
13  check "Show Lines"
14  take screenshot
15  uncheck "Show Lines"
16  take screenshot
"""

import pyautogui
import datetime
import time
import re
import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
patient = simpledialog.askstring(title="Retina Screenshots",
prompt="Patient Name/ID:") # ask user for string to append to screenshot label

datetimeObject = datetime.datetime.today()
t = str(datetimeObject.time())
pattern = r':'
modified_t = re.sub(pattern, '', t)  # replace ":" with "." using regex

pyautogui.click(x=1850, y=108) # close quickvue
time.sleep(2)
pyautogui.click(x=1835, y=453) # uncheck "show lines"
time.sleep(.3)
pyautogui.click(x=1678, y=462) # select "retina"
time.sleep(.5)
im = pyautogui.screenshot() # take screenshot 1
im.save(patient + '_1_ret_no_lines' + modified_t +'.tiff')

time.sleep(.2)
pyautogui.click(x=407, y=154) # select "measure"
time.sleep(.3)
pyautogui.moveTo(402, 185, duration=.5)
time.sleep(.2)
pyautogui.click(x=402, y=185) # select "density"
time.sleep(3)
pyautogui.click(x=1835, y=453) # check "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot 2
im.save(patient + '_2_ret_dens_sup_lines' + modified_t +'.tiff')

time.sleep(.2)
pyautogui.click(x=1835, y=453) # uncheck "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot 3
im.save(patient + '_3_ret_dens_sup_no_lines' + modified_t + '.tiff')

time.sleep(.2)
pyautogui.click(x=1444, y=414) # select "Deep"
time.sleep(.5)
pyautogui.click(x=1835, y=453) # check "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot 4
im.save(patient + '_4_ret_dens_deep_lines' + modified_t + '.tiff')

time.sleep(.2)
pyautogui.click(x=1835, y=453) # uncheck "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot 5
im.save(patient + '_5_ret_dens_deep_no_lines' + modified_t + '.tiff')

time.sleep(.2)
pyautogui.click(x=407, y=154) # select "measure"
time.sleep(.3)
pyautogui.moveTo(402, 185, duration=.5)
time.sleep(.2)
pyautogui.click(x=402, y=198) # select "faz"
time.sleep(3)
pyautogui.click(x=1835, y=453) # check "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot 6
im.save(patient + '_6_ret_faz_lines' + modified_t + '.tiff')
