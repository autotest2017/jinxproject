#!/usr/bin/env python
#encoding:utf-8


from PIL import ImageGrab
import time

def get_sceent_shot(image_name):
    shot = ImageGrab.grab()
    shot.save("./screen_shot/%s.jpg" % image_name)



if __name__ == '__main__':
    image_name = "./shot.jpg"
    get_sceent_shot(image_name)