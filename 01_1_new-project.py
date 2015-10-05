#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import os.path
import xml.etree.ElementTree as et
import cv

PROJECTS_DIR_NAME = "vagrant-data"


def main():
	print sys.argv[0]
	print os.path.split(sys.argv[0])

	if len(sys.argv) < 2:
		print "usage: ./%s movie_file"%sys.argv[0]
		return
	
	curdir = os.curdir
	
	if not os.path.isfile(sys.argv[1]):
		print "** Error: %s is not a valid filepath"%(sys.argv[1])
		return

	movie_path, movie_file = os.path.split(sys.argv[1])
	print "movie path: %s, \nfile: %s"%(movie_path, movie_file)
	
	#if movie_path != ",":
	#  os.chdir(os.path.split(movie_path)[0])

	# the project name is the movie filename without extension
	project_dir = os.path.splitext(movie_file)[0]
	print "project dir is %s"%(project_dir)

	working_dir = os.path.join(PROJECTS_DIR_NAME, project_dir)

	if not os.path.isdir(working_dir):
		print "Creating the project directory %s"%(working_dir)
		try:
			os.makedirs(working_dir)
		except:
			print "** Error: failed to create the project directory"
			return
	
	# generate project xml file:
	root = et.Element("movie")
	#root.set("title", project_dir)
	root.set("path", sys.argv[1])
	#root.set("frames", str(frame_count))
	#root.set("fps", str(fps))
	
	# wrap and save
	tree = et.ElementTree(root)
	os.chdir(working_dir)
	tree.write("project.xml")
	
	print "don't forget to crop / remove any black borders!"
	
	raw_input("- done -")
	return


# #########################
if __name__ == "__main__":
	main()
# #########################
