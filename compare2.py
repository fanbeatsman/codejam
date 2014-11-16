import os, sys
import Image

img = Image.open("subject01.happy.png")
img2 = Image.open("subject01.normal.png")
#im = img.load()
#im2 =img2.load()

likelyhood=0

pix_val = list(img.getdata())
print pix_val


