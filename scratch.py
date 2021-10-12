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
