from mss import mss
import numpy as np
from coordinate_finder import pixel_data
import pyautogui
import time
import random
import keyboard
import json
import os

monitor = {"top": pixel_data['y'], "left": pixel_data['x'], "width": 1, "height": 1}
SAVE_FILE = "procs_count.json"
offset = 0

def capture_screen():
        with mss() as sct:
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)
            b,g,r,_=frame[0,0]
            return r, g, b

def color_match(captured_color):
    r, g, b = captured_color

    return ((pixel_data['r'] -10) <= r <= (pixel_data['r']+10) and (pixel_data['g'] -10) <= g <= (pixel_data['g']+10) and (pixel_data['g'] -10) <= g <= (pixel_data['g']+10))

def load_procs():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as file:
            try:
                return json.load(file).get("procs", 0)
            except json.JSONDecodeError:
                return 0
    return 0

def save_procs(procs):
    with open(SAVE_FILE, "w") as file:
        json.dump({"procs": procs}, file)

procs = load_procs()

while True:
    capture = capture_screen()

    if color_match(capture):
        time.sleep(random.uniform(.25, .4))
        procs += 1
        save_procs(procs)
        pyautogui.rightClick()
        time.sleep(.3 + random.uniform(.1, .25))
        pyautogui.rightClick()
        #ew time.sleep(20) #uncomment for slug fish
        if (procs%2 != 0):
            offset = random.randint(1, 3)
            pyautogui.moveRel(offset, offset, .5)
        else:
            pyautogui.moveRel(-offset, -offset, .5)
        print(procs)

    time.sleep(0.05)