import pyautogui
import time
import keyboard
from mss import mss
import numpy as np

#uncomment following line and substitute values printed
pixel_data = {"x": 1103,"y": 699,"r": 249,"g": 83,"b":83}

def get_mouse_position_and_color():
    print("Mouse position and color capturing. Press 'q' to stop.")

    monitor = {"top": 0, "left": 0, "width": 1, "height": 1}

    while True:
        #get mouse position
        x, y = pyautogui.position()

        with mss() as sct:
            monitor["top"] = y  #updates monitor to mouse position
            monitor["left"] = x  #updates monitor to mouse position
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)
            b, g, r, _ = frame[0, 0]  #get color at mouse position

        #terminator
        if keyboard.is_pressed("q"):
            print("\nCapture stopped.")
            return {"x": x, "y": y, "color": {"r": r, "g": g, "b": b}}

        time.sleep(0.1)

if __name__ == "__main__":

    result = get_mouse_position_and_color()

    #trim data
    x = result['x']
    y = result['y']
    r = int(result['color']['r'])
    g = int(result['color']['g'])
    b = int(result['color']['b'])

    print(f"X: {x}, Y: {y}")
    print(f"R: {r}, G: {g}, B: {b}")

