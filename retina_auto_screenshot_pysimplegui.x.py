"""
RAPID ACQUISITION OF SCREENSHOTS IN REQUIRED ORIENTATIONS,
SAVED OUT TO THE FOLDER WHERE THE SCRIPT IS LOCATED

1- Load a volume, 2- Run the retina or disk script, 3- Enter patient name & volume number
  [AUTOMATED STEPS]
3- close QuickVue     4- uncheck "Show Lines"     5- select "Retina"     6- take screenshot 1
7- select "Measure\Density"    8- check "Show Lines"    9- take screenshot 2
10- uncheck "Show Lines"   11- take screenshot 3
12- select "Deep"   13- check "Show Lines"    14-take screenshot 4
15- uncheck "Show Lines"    16- take screenshot 5
17- check "Show Lines"    18- take screenshot 6 """

import pyautogui
import time
import tkinter as tk
from tkinter import simpledialog
import tkinter.messagebox
import PySimpleGUI as sg   
  
ROOT = tk.Tk()
ROOT.withdraw()


"""
PySimpleGUI - Form to request patient name/ID & volume # 
"""

layout = [[sg.Text('Please enter the Patient Name & Volume number')],
          [sg.Text('Name', size=(10, 1)), sg.InputText(key='-NAME-')],
          [sg.Text('Vol #', size=(10, 1)), sg.InputText(key='-VOL-')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

window = sg.Window('Auto-Screenshot - Retina', layout)
event, values = window.read(close=True)

if event == 'Submit':
    patient = values['-NAME-']
    volume = values['-VOL-']
else:
  print('User cancelled')
  exit()

# Begin acquiring screenshots

pyautogui.click(x=1850, y=108) # close quickvue
time.sleep(2)
pyautogui.click(x=1835, y=453) # uncheck "show lines"
time.sleep(.3)
pyautogui.click(x=1678, y=462) # select "retina"
time.sleep(.5)
im = pyautogui.screenshot() # take screenshot 1
im.save(patient + '_vol_' + volume + '_screenshot_1_ret_no_lines' + '.tiff')

# time.sleep(.2)
# pyautogui.click(x=407, y=154) # select "measure"
# time.sleep(.3)
# pyautogui.moveTo(402, 185, duration=.5)
# time.sleep(.2)
# pyautogui.click(x=402, y=185) # select "density"
# time.sleep(3)
# pyautogui.click(x=1835, y=453) # check "show lines"
# time.sleep(.2)
# im = pyautogui.screenshot() # take screenshot 2
# im.save(patient + '_vol_' + volume + '_screenshot_2_ret_dens_sup_lines' + '.tiff')

# time.sleep(.2)
# pyautogui.click(x=1835, y=453) # uncheck "show lines"
# time.sleep(.2)
# im = pyautogui.screenshot() # take screenshot 3
# im.save(patient + '_vol_' + volume + '_screenshot_3_ret_dens_sup_no_lines' + '.tiff')

# time.sleep(.2)
# pyautogui.click(x=1444, y=414) # select "Deep"
# time.sleep(.5)
# pyautogui.click(x=1835, y=453) # check "show lines"
# time.sleep(.2)
# im = pyautogui.screenshot() # take screenshot 4
# im.save(patient + '_vol_' + volume + '_screenshot_4_ret_dens_deep_lines' + '.tiff')

# time.sleep(.2)
# pyautogui.click(x=1835, y=453) # uncheck "show lines"
# time.sleep(.2)
# im = pyautogui.screenshot() # take screenshot 5
# im.save(patient + '_vol_' + volume + '_screenshot_5_ret_dens_deep_no_lines' + '.tiff')

# time.sleep(.2)
# pyautogui.click(x=407, y=154) # select "measure"
# time.sleep(.3)
# pyautogui.moveTo(402, 185, duration=.5)
# time.sleep(.2)  
# pyautogui.click(x=402, y=198) # select "faz"
# time.sleep(3)
# pyautogui.click(x=1835, y=453) # check "show lines"
# time.sleep(.2)
# im = pyautogui.screenshot() # take screenshot 6
# im.save(patient + '_vol_' + volume + '_screenshot_6_ret_faz_lines' + '.tiff')

tkinter.messagebox.showinfo('Retina','Finished')
ROOT.mainloop()