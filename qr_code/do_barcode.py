#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install pyBarcode
# pip install Pillow
from barcode.writer import ImageWriter
from barcode.codex import Code39
from PIL import Image, ImageDraw, ImageFont, ImageWin

imagewriter = ImageWriter()
ean = Code39('1234567890', writer=imagewriter, add_checksum=False)
fullname = ean.save('barcode')
img = Image.open(fullname)
img.show()
