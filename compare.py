from PIL import Image, ImageChops
import sys
import os
import time
#import pprint

"""Usage: python compare.py [directory of pictures to match] [path to 1 picture you want to try matching]"""

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
current_winner=["none",0]#current_winner keeps track of the image with highest match score up to date
target = Image.open(sys.argv[2])

#main method
ticks_start=time.time()
for (dirpath,dirnames,filenames) in os.walk(sys.argv[1]): #goes through the whole directory
	for filename in filenames:
		match=0 #match is a score, the higher it is, the better 2 pictures match each other
		print (os.sep.join([dirpath, filename]))
		try:
			candidate = Image.open(os.sep.join([dirpath, filename]))
			difference = black_or_b(target,candidate)
			difference.save('difference.png') #saves an image that is the graphical difference of both images
               		difference_pixels = difference.getdata()
               		height = difference_pixels.size[1] #need height and maybe for the future to handle the situation where a person's face is exactly the same but is shifted
               		width = difference_pixels.size[0]
               		difference_pixels = list(difference_pixels)
               		difference_pixels = list(chunks(difference_pixels,3))
                	difference_pixels = chunks(difference_pixels,width)
			

			for row in difference_pixels:
	                        for rgb in row:
	                                avg = sum(rgb)/3
	                                if avg<50:#tweakable arbitrary number 50 that determines how "exact" a match has to be
        	                                match=match+1
        	        #                        print match #comment this out so the program doesnt log everything, might make runtime faster
        	        if (match > current_winner[1]):
                	        current_winner=[filename,match]



		except:
			print ("error")


ticks_stop = time.time()
runtime = ticks_stop-ticks_start
print current_winner
print ("Done in:")
print runtime, " ticks"
