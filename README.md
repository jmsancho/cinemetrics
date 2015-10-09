Cinemetrics
===========
The initial code for this project was Frederic Brodbeck's bachelor graduation project at the Royal Academy of Arts (KABK), Den Haag code.  http://cinemetrics.fredericbrodbeck.de/

## The Idea
Cinemetrics is about measuring and visualizing movie data, in order to reveal the characteristics of films and to create a visual “fingerprint” for them. Information such as the editing structure, color, speech or motion are extracted, analyzed and transformed into graphic representations so that movies can be seen as a whole and easily interpreted or compared side by side.

# Requirements
* [Vagrant](http://www.VagrantUp.com)
    * Fingers crossed, that's all you should need! The goal of this fork is to wrap all the dependencies needed for cinemetrics into a reusable, cross-platform Vagrantfile.
 
# Installation
* Clone the repo to your local machine or grab the latest release.

# Usage
* Go to the repo folder in terminal 
```
vagrant up
```
    * That should run the provisioning shell script which will install (if everything goes according to plan...) all the necessary dependencies.
* Place your video file inside the vagrant-data folder.
* SSH into the Vagrant instance
```
vagrant ssh
```
* cd to the main project folder
```
cd /vagrant
```
* With the your video file in place, work through each python file starting with 01_1_new-project.py. The syntax for your first command should look like:
```
$ python 01_1_new-project.py vagrant-data/THE_NAME_OF_YOUR_VIDEO_FILE.mp4
```

Feel free to open an issue if you have any trouble or even better, create a pull request for improvements to the code!
