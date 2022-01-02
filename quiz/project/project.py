#Write the random number generator in Python. It must use some physical elements.
#You can use voice, mouse moves, CPU rate or any other physical structures for implementing it. 
#The length of the random number must bit 16 bits. Use the needed libraries.

from pynput.mouse import Listener
import random


def on_click(x, y, button, pressed):
    if pressed:
        print(random.getrandbits(16))


with Listener(on_click=on_click) as listener:
    listener.join()
