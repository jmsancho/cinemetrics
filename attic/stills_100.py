# -*- coding: utf-8 -*-
import cv
import math
import os
import sys
import xml.etree.ElementTree as et
import utils

OUTPUT_DIR = "100_stills"


def main():

	tree = utils.open_project(sys.argv)
	if tree == None:
		return

	try:
		os.mkdir(OUTPUT_DIR)
	except OSError:
		pass


	movie = tree.getroot()
	file_path = movie.attrib["path"]
<<<<<<< HEAD:02_5_100-stills.py
	#fps = float( movie.attrib["fps"] )

=======
	fps = float( movie.attrib["fps"] )
	
>>>>>>> parent of 1f8384f... minor changes:stills_100.py
	cap = cv.CreateFileCapture(file_path)
	cv.QueryFrame(cap)

	# skip frames in the beginning, if neccessary
	start_frame = int( movie.attrib["start_frame"] )
	for i in range(start_frame):
		cv.QueryFrame(cap)

	end_frame = int( movie.attrib["end_frame"] )
	every_nth_frame = int( (end_frame - start_frame) / 100 )
<<<<<<< HEAD:02_5_100-stills.py
	print("every {} frames".format(every_nth_frame))
	#print "=", every_nth_frame / fps, "sec"
=======
	print "every", every_nth_frame, "frames"
	print "=", every_nth_frame / fps, "sec"
>>>>>>> parent of 1f8384f... minor changes:stills_100.py
	frame = start_frame

	for counter in range(1, end_frame):
		print(counter)
		img = cv.QueryFrame(cap)
		if not img:
			break
<<<<<<< HEAD:02_5_100-stills.py

		img_small = cv.CreateImage((WIDTH, int( img.height * float(WIDTH)/img.width )), cv.IPL_DEPTH_8U, 3)
		cv.Resize(img, img_small, cv.CV_INTER_CUBIC)

		cv.SaveImage(os.path.join(OUTPUT_DIR,"still_%07d.jpg" % (frame)), img_small)

=======
		
		cv.SaveImage(OUTPUT_DIR + "\\still_%07d.jpg" % (frame), img)
		
>>>>>>> parent of 1f8384f... minor changes:stills_100.py
		for i in range(every_nth_frame-1):
			cv.GrabFrame(cap)

		frame += every_nth_frame
<<<<<<< HEAD:02_5_100-stills.py

	#raw_input("- done -")
=======
		counter += 1
	
	raw_input("- done -")
>>>>>>> parent of 1f8384f... minor changes:stills_100.py
	return


# #########################
if __name__ == "__main__":
	main()
# #########################
