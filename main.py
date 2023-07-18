import PIL.Image
import numpy as np
import random
from tkinter import *


def create_rbg():
    image = np.array(PIL.Image.open('landscape.jpg'))
    rbg_list = []

    for _ in range(1, 10):
        y = image.shape[0] - 1
        x = image.shape[1] - 1
        random_y = random.randint(0, y)
        random_x = random.randint(0, x)
        r, g, b = image[random_y, random_x]
        rbg_list.append([r, g, b])

    return rbg_list


def rgb_to_hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


window = Tk()

i = 0
for rgb in create_rbg():

    colour = Canvas(window, width=60, height=60, bg=rgb_to_hex(create_rbg()[i][0], create_rbg()[i][1],
                                                               create_rbg()[i][2]))
    colour.create_text(32, 20, text=f"{rgb_to_hex(create_rbg()[i][0], create_rbg()[i][1], create_rbg()[i][2])}")
    colour.pack()
    i += 1


window.mainloop()
