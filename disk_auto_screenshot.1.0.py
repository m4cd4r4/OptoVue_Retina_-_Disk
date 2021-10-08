import pyautogui
import time

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
