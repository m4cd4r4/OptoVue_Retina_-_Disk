import pyautogui
import datetime
import time

import re

import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()
ROOT.withdraw()
patient = simpledialog.askstring(title="Retina Screenshots",
                                  prompt="Patient Name/ID:")

datetimeObject = datetime.datetime.today()
t = str(datetimeObject.time())
pattern = r':'
mod_t = re.sub(pattern, '', t)

pyautogui.click(x=1850, y=108) # close quickvue
time.sleep(2)
pyautogui.click(x=407, y=154) # select "measure"
time.sleep(.3)
pyautogui.click(x=402, y=182) # select "density"
time.sleep(3)
pyautogui.click(x=1835, y=453) # check "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot
im.save('7_disc_density_show_lines' + '.tiff') 
time.sleep(.2)
pyautogui.click(x=1835, y=453) # uncheck "show lines"
time.sleep(.2)
im = pyautogui.screenshot() # take screenshot
im.save('8_disc_density_no_lines' + '.tiff') 
