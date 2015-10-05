#!/bin/sh

# Update the package manager and install some base software
apt-get update
apt-get -y install vim git screen

# install primary dependencies listed on github
echo "Installing primary dependencies..."
apt-get -y install python-opencv build-essential checkinstall git cmake libfaac-dev libjack-jackd2-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libsdl1.2-dev libtheora-dev libva-dev libvdpau-dev libvorbis-dev libx11-dev libxfixes-dev libxvidcore-dev texi2html yasm zlib1g-dev python-numpy python-scipy python-matplotlib