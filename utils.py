import os
import xml.etree.ElementTree as et


def open_project(argv, print_usage=True):
    
    if len(argv) < 2:
        print "usage: %s project_dir"%(argv[1])
        return None

    path = argv[1]

    if not os.path.isdir(path):
        print "** Error: invalid project directory %s"%(path)
        return None

    os.chdir(path)

    if not os.path.isfile("project.xml"):
        print "** Error: could not find project.xml, did you use 01_1_new-project first?"
        return None

    return et.parse("project.xml")
