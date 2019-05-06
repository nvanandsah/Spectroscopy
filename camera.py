import picamera 
import time
import numpy
import cv2

count = 0
camera = picamera.PiCamera()
#camera.shutter_speed = 10000
# camera.resolution = (416,800)
stream = cv2.VideoCapture()
s = 1;
t = time.time()
while (s) :
	s,image = stream.read()
	cv2.imwrite("pictures/frame" + str(count) + ".jpg", image)
	count +=1
	if (count == 100):
		break
camera.close()
done = time.time() - t
print('time taken: ' + str(done))
