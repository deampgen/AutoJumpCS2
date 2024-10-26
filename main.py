import time
import keyboard
TICK_64_MS = 0.0156
exit_key = "end"
activation_key = "space"
toggle_key = "+"
toggle = True
def send_space(duration):
    keyboard.send("space")
    time.sleep(duration)
keyboard.add_hotkey(exit_key, lambda: exit())
while True:
    if keyboard.is_pressed(activation_key):
        if toggle:
            send_space(TICK_64_MS * 1)
 
            while keyboard.is_pressed(activation_key):
                send_space(TICK_64_MS * 2)
    elif keyboard.is_pressed(toggle_key):
        toggle = not toggle
        time.sleep(0.2) 
    else:
        time.sleep(0.001)
exit()
