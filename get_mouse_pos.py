import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        
        print(f"Mouse coordinates: X={x}, Y={y}")

except KeyboardInterrupt:
    pass
