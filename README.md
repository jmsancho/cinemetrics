Cinemetrics
===========

This code is part of http://cinemetrics.fredericbrodbeck.de/

Cinemetrics is about measuring and visualizing movie data, in order to reveal the characteristics of films and to create a visual "fingerprint" for them. Information such as the editing structure, color, speech or motion are extracted, analyzed and transformed into graphic representations so that movies can be seen as a whole and easily interpreted or compared side by side.

~~At the moment these tools lack proper documentation, sorry.~~ Expanding documentation.


Requirements
------------

 * opencv http://opencv.willowgarage.com/wiki/
 * ffmpeg
 * numpy
 * scipy
 * colormath https://pypi.python.org/pypi/colormath
 * matplotlib
 
 -----------
 # Installation
 ## Mac (10.10 & Python 2.7.6)
* Clone the repo to your local machine. 
* Download dependencies 
  * Working to add these as submodules so you should be able to get up and running faster. For a quick overview of submodules - http://blog.sourcetreeapp.com/2012/02/01/using-submodules-and-subrepositories/ - of course nothing is that easy...
    * opencv: 
    
 
 ## Debian/Ubuntu/Mint
 ------------------
 
```
apt-get install python-opencv ffmpeg build-essential checkinstall git cmake libfaac-dev libjack-jackd2-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libsdl1.2-dev libtheora-dev libva-dev libvdpau-dev libvorbis-dev libx11-dev libxfixes-dev libxvidcore-dev texi2html yasm zlib1g-dev python-numpy python-scipy python-matplotlib
```

* gstreamer
  ``` 
  apt-get install libgstreamer0.10-0 libgstreamer0.10-dev gstreamer0.10-tools gstreamer0.10-plugins-base libgstreamer-plugins-base0.10-dev gstreamer0.10-plugins-good gstreamer0.10-plugins-ugly gstreamer0.10-plugins-bad gstreamer0.10-ffmpeg
  ```
* libjpg
  ```
  apt-get install libjpeg8 libjpeg8-dev
  ```

----------
