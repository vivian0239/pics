import digitalio
import board
import time
backlight = digitalio.DigitalInOut(board.D21)
backlight.switch_to_output()
for i in range(10):
    backlight.value = False
    time.sleep(1)
    backlight.value = True
    time.sleep(1)
