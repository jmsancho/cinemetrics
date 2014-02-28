#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  makeCUE.py
#
#  Copyright 2014 Coren <Coren.mail@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

from datetime import datetime
import re, sys
import argparse

def loadChapters(chapter_file):
    '''
    Read an eac3to chapters file and extracts indices, timestamps and
    track titles.

    A chapter file should look something like this:

    '''

    example = '''
    Invalid chapter file. Chapters should have the following format:

    CHAPTER01=00:00:00.000
    CHAPTER01NAME=
    CHAPTER02=00:18:42.121
    CHAPTER02NAME=
    CHAPTER03=00:28:54.733
    CHAPTER03NAME=
    '''

    with open(chapter_file, 'r') as fin:
        lines = [line.strip() for line in fin.readlines() if line.strip()]

    re_stamp = re.compile('CHAPTER(\d\d)=(\d\d:\d\d:\d\d.\d\d\d)')
    re_name = re.compile('CHAPTER(\d\d)NAME=(.*)')

    chapters = {}
    for line in lines:
        assert line.startswith('CHAPTER'), 'Invalid chapter file. Every line should start with CHAPTER??'

        if re.match(re_stamp, line):
            found = re.match(re_stamp, line).groups()
            assert len(found) == 2, example
            num, stamp = int(found[0]), datetime.strptime(found[1], '%H:%M:%S.%f')
            assert num not in chapters, 'Invalid chapter file. Each chapter should only occur once.'
            chapters[num] = [stamp]

        elif re.match(re_name, line):
            found = re.match(re_name, line).groups()
            assert len(found) == 2, example
            num, name = int(found[0]), found[1]
            assert num in chapters, example
            if name.strip():
                chapters[num].append(name)
            else:
                chapters[num].append('')

        else:
            sys.exit(msg=example)

    return chapters


def getFrames(stamp, fps):
    frm = int(stamp.microsecond/float(1000))
    # print(frm)
    total_sec = (stamp.hour * 60 * 60) + (stamp.minute * 60) + stamp.second
    frames = (total_sec * fps) + frm
    # print(frames)
    return int(frames)


def printFrames(chapters, fps):
    '''
    Input:
    a dictionary of {chapter_number: [datetime_stamp, track_title}
    '''
    for num in range(1, len(chapters)+1):

        stamp = chapters[num][0]
        print(getFrames(stamp, fps))
        # hundreths = int(stamp.microsecond/float(10000))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Convert a eac3to chapter file to a list of frames.')
    parser.add_argument('chapter_file', metavar='chapter_file', type=str,
                       help='The chapter file from eac3to')
    parser.add_argument('fps', metavar='fps', type=float,
                       help='Frames per seconds')

    args = parser.parse_args()

    chapters = loadChapters(args.chapter_file)
    printFrames(chapters, args.fps)
