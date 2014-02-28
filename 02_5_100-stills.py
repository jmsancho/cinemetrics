# -*- coding: utf-8 -*-
import cv
import math
import os
import sys
import xml.etree.ElementTree as et
import utils

OUTPUT_DIR = "100_stills"
WIDTH = 240


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
	#fps = float( movie.attrib["fps"] )

	cap = cv.CreateFileCapture(file_path)
	cv.QueryFrame(cap)

	# skip frames in the beginning, if neccessary
	start_frame = int( movie.attrib["start_frame"] )
	for i in range(start_frame):
		cv.QueryFrame(cap)

	end_frame = int( movie.attrib["end_frame"] )
	every_nth_frame = int( (end_frame - start_frame) / 100 )
	print("every {} frames".format(every_nth_frame))
	#print "=", every_nth_frame / fps, "sec"
	frame = start_frame

	for counter in range(1, end_frame):
		print(counter)
		img = cv.QueryFrame(cap)
		if not img:
			break

		img_small = cv.CreateImage((WIDTH, int( img.height * float(WIDTH)/img.width )), cv.IPL_DEPTH_8U, 3)
		cv.Resize(img, img_small, cv.CV_INTER_CUBIC)

		cv.SaveImage(os.path.join(OUTPUT_DIR,"still_%07d.jpg" % (frame)), img_small)

		for i in range(every_nth_frame-1):
			cv.GrabFrame(cap)

		frame += every_nth_frame

	#raw_input("- done -")
	return


# #########################
if __name__ == "__main__":
	main()
# #########################
