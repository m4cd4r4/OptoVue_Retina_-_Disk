"""
1   User - choose patient & load a "retina" volume

    (Automated:)

2   Ask user to input patient name/patient ID & volume #
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
import tkinter.messagebox

ROOT = tk.Tk()
ROOT.withdraw()

patient = simpledialog.askstring(title="Retina Screenshots",
prompt="Patient Name/ID:") # ask user for string to append to screenshot label

volume = simpledialog.askstring(title="Retina Screenshots",
prompt="Volume #:") # ask user for volume number (1, 2, 3 etc)

pyautogui.click(x=1850, y=108) # close quickvue
time.sleep(2)
pyautogui.click(x=1835, y=453) # uncheck "show lines"
time.sleep(.3)
pyautogui.click(x=1678, y=462) # select "retina"
time.sleep(.5)
im = pyautogui.screenshot() # take screenshot 1
im.save(patient + '_vol_' + volume + '_screenshot_1_ret_no_lines' + '.tiff')

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
im.save(patient + '_vol_' + volume + '_screenshot_2_ret_dens_sup_lines' + '.tiff')

time.sleep(.2)
pyautogui.click(x=1835, y=453) # uncheck "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot 3
im.save(patient + '_vol_' + volume + '_screenshot_3_ret_dens_sup_no_lines' + '.tiff')

time.sleep(.2)
pyautogui.click(x=1444, y=414) # select "Deep"
time.sleep(.5)
pyautogui.click(x=1835, y=453) # check "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot 4
im.save(patient + '_vol_' + volume + '_screenshot_4_ret_dens_deep_lines' + '.tiff')

time.sleep(.2)
pyautogui.click(x=1835, y=453) # uncheck "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot 5
im.save(patient + '_vol_' + volume + '_screenshot_5_ret_dens_deep_no_lines' + '.tiff')

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
im.save(patient + '_vol_' + volume + '_screenshot_6_ret_faz_lines' + '.tiff')

tkinter.messagebox.showinfo('Screenshots - Retina','Finished')
ROOT.mainloop()