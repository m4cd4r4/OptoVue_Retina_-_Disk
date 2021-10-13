"""
Author: Macdara O Murchu - Physiology & Pharmacology Dept, LEI
v1.2 - replaced regex & timestamp with "pysimplegui" uniquely identifying patient info

FAST ACQUISITION OF SCREENSHOTS IN SPECIFIC ORIENTATIONS,
SAVED OUT TO THE FOLDER WHERE THE SCRIPT IS LOCATED,
LABELLED AS "[PATIENT]_[VOLUME]_[SCREENSHOT# & ORIENTATION].TIFF"

1- Load a volume, 2- Run the retina or disk script, 3- Enter patient name & volume number
  [AUTOMATED STEPS]
3- close QuickVue     4- uncheck "Show Lines"     5- select "Retina"     6- take screenshot 1
7- select "Measure\Density"    8- check "Show Lines"    9- take screenshot 2
10- uncheck "Show Lines"   11- take screenshot 3
12- select "Deep"   13- check "Show Lines"    14-take screenshot 4
15- uncheck "Show Lines"    16- take screenshot 5
17- check "Show Lines"    18- take screenshot 6 
"""
import pyautogui as pag
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

window = sg.Window('Auto-Screenshot - Disc', layout)
event, values = window.read(close=True)

if event == 'Submit':
    patient = values['-NAME-']
    volume = values['-VOL-']
else:
  print('User cancelled')
  exit()

# Begin acquiring screenshots

pag.click(x=1850, y=108) # close quickvue
time.sleep(2)
pag.click(x=407, y=154) # select "measure"
time.sleep(.3)
pag.click(x=402, y=182) # select "density"
time.sleep(3)
pag.click(x=1835, y=453) # check "show lines"
time.sleep(.2)
im = pag.screenshot() # take screenshot

im.save(patient + '_vol_' + volume + '_screenshot_7_disc_dens_lines' + '.tiff') 
time.sleep(.2)
pag.click(x=1835, y=453) # uncheck "show lines"
time.sleep(.2)
im = pag.screenshot() # take screenshot
im.save(patient + '_vol_' + volume + '_screenshot_8_disc_dens_lines' + '.tiff') 

tkinter.messagebox.showinfo('Disc','Finished')
ROOT.mainloop()