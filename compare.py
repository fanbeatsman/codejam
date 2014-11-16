from PIL import Image, ImageChops
import sys
import os
import time
#import pprint

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

point_table = ([0] + ([255] * 255))

def black_or_b(a, b):
    diff = ImageChops.difference(a, b)
    return diff


currentdir = os.getcwd()
current_winner=["none",0]
target = Image.open(sys.argv[2])

#main method
ticks_start=time.time()
for (dirpath,dirnames,filenames) in os.walk(sys.argv[1]):
	for filename in filenames:
		match=0
		print (os.sep.join([dirpath, filename]))
		try:
			candidate = Image.open(os.sep.join([dirpath, filename]))
			difference = black_or_b(target,candidate)
			difference.save('difference.png')
               		difference_pixels = difference.getdata()
               		height = difference_pixels.size[1]
               		width = difference_pixels.size[0]
               		difference_pixels = list(difference_pixels)
               		difference_pixels = list(chunks(difference_pixels,3))
                	difference_pixels = chunks(difference_pixels,width)
			

			for row in difference_pixels:
	                        for rgb in row:
	                                avg = sum(rgb)/3
	                                if avg<50:
        	                                match=match+1
        	        #                        print match #comment this out so the program doesnt log everything, might make runtime faster
        	        if (match > current_winner[1]):
                	        current_winner=[filename,match]



		except:
			print ("error")


#a = Image.open('1_10_.gif')
#b = Image.open('12_7_.gif')
#c = black_or_b(a, b)
#c.save('c.png')


#c_pixels=list(imread("c.png").astype(int))

#c_pixels = c.getdata()
#height=c_pixels.size[1]
#width=c_pixels.size[0]


#print width
#c_pixels=list(c_pixels)
#c_pixels = list(chunks(c_pixels,3))
#c_pixels = chunks(c_pixels,width)

#print c_pixels

#for row in c_pixels:
#	for rgb in row:
#		avg = sum(rgb)/3
#		if avg<50:
#			likeness=likeness+1
ticks_stop = time.time()
runtime = ticks_stop-ticks_start
print current_winner
print ("Done in:")
print runtime, " ticks"
