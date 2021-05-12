import time
import threading
from pynput.mouse import Button
from pynput.keyboard import Listener, keyCode

delay = 0.01
button = Button.left
sart_stop_key = Keycode(char = 's')
exit_key = KeyCOde(char + 'e')

class Clickmouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(selfself):
        self.running = True

    def stop_running(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)

mouse = controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click.thread.start_clicking()

    elif key == exit_key:
        clcik_thread.exit()
        listener.stop()

with Listener(on_press = on_press) as listener:
    Listener.join()
    