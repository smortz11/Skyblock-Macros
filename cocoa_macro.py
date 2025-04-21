import ctypes
import time

VK_Q = 0x51
KEYEVENTF_KEYUP = 0x0002

class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))
    ]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("ki", KEYBDINPUT)]
    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_ulong), ("_input", _INPUT)]

def press_key(hex_key_code):
    x = INPUT(type=1)
    x.ki = KEYBDINPUT(hex_key_code, 0, 0, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def release_key(hex_key_code):
    x = INPUT(type=1)
    x.ki = KEYBDINPUT(hex_key_code, 0, KEYEVENTF_KEYUP, 0, None)
    ctypes.windll.user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

print("Switch to Notepad now. Pressing Q in 3 seconds...")
time.sleep(3)
press_key(VK_Q)
time.sleep(0.2)
release_key(VK_Q)
print("Done.")
