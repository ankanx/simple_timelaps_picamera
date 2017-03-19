# Created by: Andreas Fransson 

import picamera
import time
import datetime
import os

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
camera.start_preview()

global directory

while True:

        todaysDate= time.strftime("%d-%m-%y")
        directory = '/home/pi/camera/storage/' + todaysDate
        
        if not os.path.exists(directory):
                os.makedirs(directory)
                #print 'made daily dir'

        timeStamp = datetime.datetime.utcnow()
        camera.annotate_text = timeStamp.strftime('%Y-%m-%d %H:%M:%S')
        time.sleep(300)
        #print 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcnow())

        camera.capture(directory + '/' + timeStamp.strftime('%Y-%m-%d-%H-%M-%S')+'.jpg')
        #print 'saved ' + directory + '/' + timeStamp.strftime('%Y-%m-%d-%H-%M-%S')+'.jpg'

