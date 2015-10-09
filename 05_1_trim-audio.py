# -*- coding: utf-8 -*-
import sys
import scipy.io.wavfile
import xml.etree.ElementTree as et
import os


def main():
	os.chdir(sys.argv[1])

	tree = et.parse("project.xml")
	movie = tree.getroot()
	path = movie.attrib["path"]
	path = os.path.dirname(path)
	fps = float( movie.attrib["fps"] )
	start_frame = int( movie.attrib["start_frame"] )
	end_frame = int( movie.attrib["end_frame"] )

	# os.chdir(path)
	file = os.path.join(path, "audio.wav")
	rate = scipy.io.wavfile.read(file, mmap=True)
	print("{} hz".format(rate))

	print(start_frame, fps, rate[0])
	trim_from = int( (start_frame / fps) * rate[0] )
	trim_to   = int( (end_frame / fps) * rate[0] )
	os.system("sox ../audio.wav ../audio_trimmed.wav trim %ds %ds" % (trim_from, trim_to))
	print start_frame, end_frame
	print trim_from, trim_to
	print ("Audio trim complete.")


# #########################
if __name__ == "__main__":
	main()
# #########################
