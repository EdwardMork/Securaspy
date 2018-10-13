# Securaspy
Some l33t code to record ding-dong ditchers at my house


## Motivation
Ever get tired of people ding dong ditching your house? Now you can create a system that will record these little rascals so you can tell them to get off your lawn!

Not only am I motivated by ding dong ditchers, but am also looking into digital image processing techniques. More specfically motion detection and tracking. 

## Materials

* Raspberry Pi 3
* Raspberry Pi compatible camera
* HC-SR04 Ultrasonic Range finder
* Breadboard
* Jumper wires 

## Methodology
There are two python files within this repository:  
## sensor.py
This python script makes use of a ultrasonic range finder in order to detect obstacles in the path. The ultrasonic was used to test the camera on a Raspberry Pi.
Wiring for the ultrasonic range finder was completed using <a href="https://www.modmypi.com/image/data/tutorials/hc-sr04/hc-sr04-tut-2.png"> this </a> image.

## motion.py
Motion.py uses OpenCV to analyze frame by frame images for motion. It makes use of background subtractions and Guassian Blur to detect motion within an image. The code for this was inspired by an online tutorial <a href="http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/" > here</a>


## Setup

### Prerequisites

In order to run the code one must have the following installed on their Pi: 

- Python 2.7+ (Installed on Raspbian by default) 
- OpenCV for Raspbian or other ARM OS
- PiCamera library (Installed on Raspbian by default) 

### Installing OpenCV for 

The installation of OpenCV is not trivial in regard to the Raspbian OS. A useful tutorial I used was found at this link:
<a href="https://tutorials-raspberrypi.com/installing-opencv-on-the-raspberry-pi/"> Install OpenCV for Raspberry Pi</a>

