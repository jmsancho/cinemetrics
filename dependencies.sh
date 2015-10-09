#!/bin/sh

# Update the package manager and install some base software
apt-get update
apt-get -y install vim git screen

# install primary dependencies listed on github
echo "Installing primary dependencies..."
apt-get -y install python-opencv build-essential checkinstall git cmake libfaac-dev libjack-jackd2-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libsdl1.2-dev libtheora-dev libva-dev libvdpau-dev libvorbis-dev libx11-dev libxfixes-dev libxvidcore-dev texi2html yasm zlib1g-dev python-numpy python-scipy python-matplotlib

# install gstream dependencies 
echo "Installing gstream dependencies..."
apt-get -y install libgstreamer0.10-0 libgstreamer0.10-dev gstreamer0.10-tools gstreamer0.10-plugins-base libgstreamer-plugins-base0.10-dev gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly gstreamer0.10-plugins-bad gstreamer0.10-ffmpeg

# install libjpg dependencies
echo "Installing libjpg dependencies..."
apt-get -y install libjpeg8 libjpeg8-dev

# install missing items not listed on github
echo "Installing yet more dependencies..."
apt-get -y install imagemagick python-pip sox python-nltk

# install colormath
echo "Installing colormath..."
sudo pip install colormath