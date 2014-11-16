from PIL import Image, ImageChops
from scipy.misc import imread
#import pprint

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

point_table = ([0] + ([255] * 255))

def black_or_b(a, b):
    diff = ImageChops.difference(a, b)
    print diff
    return diff

a = Image.open('subject01.normal.png')
b = Image.open('subject01.happy.png')
c = black_or_b(a, b)
c.save('c.png')

likeness=0

#c_pixels=list(imread("c.png").astype(int))

c_pixels = c.getdata()
height=c_pixels.size[1]
width=c_pixels.size[0]


print width
c_pixels=list(c_pixels)
c_pixels = list(chunks(c_pixels,3))
c_pixels = chunks(c_pixels,width)

print c_pixels

for row in c_pixels:
	for rgb in row:
		print rgb
		avg = sum(rgb)/3
		if avg<50:
			likeness=likeness+1


print likeness
if (likeness > 19500):
	print ("yes")
else:
	print ("no")
print width
print height	
