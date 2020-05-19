#!/usr/bin/env python3

from PIL import Image
im = Image.open("./IMG_3985.jpeg")
im.rotate(45).show()
