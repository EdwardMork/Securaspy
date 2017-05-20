import RPi.GPIO as GPIO
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from picamera import PiCamera
from time import sleep
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG=23
ECHO=24
camera=PiCamera()

print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

while True:
    GPIO.output(TRIG,False)
    #print "waiting for sensor to settle "
    time.sleep(0.1)

    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)

    while GPIO.input(ECHO)== 0:
                     pulse_start=time.time()

    while GPIO.input(ECHO) == 1:
                     pulse_end = time.time()

    pulse_duration = pulse_end -pulse_start

    distance = pulse_duration * 17150

    distance= round(distance,2)
    print(distance)
    if distance <= 150.0:
        print("Capturing image")
        imaage = str(datetime.now() )
        imageName = imaage + ".jpeg"
        camera.capture(imageName,format='jpeg')
        img=mpimg.imread(imageName)
        imgplot = plt.imshow(img)
        plt.ion()
        plt.show()
        plt.clf()
        plt.close()
        time.sleep(5)
GPIO.cleanup()


