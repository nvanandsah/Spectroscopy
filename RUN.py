from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy
 

camera = PiCamera()
camera.resolution = (640, 480)
#camera.shutter_speed = 100
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(640, 480))
#rawCapture = PiRGBArray(camera)
count = 0
t = time.time()

time.sleep(0.1)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	img = frame.array
	#cv2.imshow("response", image)
	#cv2.imwrite("pictures/frame" + str(count) + ".jpg", img)
	
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
	
	lower_red = numpy.array([0,50,50]) 
	upper_red = numpy.array([10,255,255]) 
	
	lower_red2 = numpy.array([165,50,50]) 
	upper_red2 = numpy.array([180,255,255])
	
	maskR = cv2.inRange(hsv, lower_red, upper_red)
	maskR2 = cv2.inRange(hsv, lower_red2, upper_red2)
	
	res_red = cv2.bitwise_and(img,img, mask = maskR) 
	res2_red = cv2.bitwise_and(img,img,mask = maskR2)
		
	lower_blue = numpy.array([105,50,50])
	upper_blue = numpy.array([127,255,255])
	
	maskB = cv2.inRange(hsv,lower_blue,upper_blue)
	
	res_blue = cv2.bitwise_and(img,img, mask = maskB)
	
	lower_green = numpy.array([44,50,50])
	upper_green = numpy.array([70,255,255])
	
	maskG = cv2.inRange(hsv,lower_green, upper_green)
	
	res_green = cv2.bitwise_and(img,img, mask = maskG)
	

	
	cv2.imshow('frame',img) 
	cv2.imshow('maskR',maskR+maskR2) 
	cv2.imshow('resR',res_red+res2_red)
	
	cv2.imshow('maskB', maskB)
	cv2.imshow('maskG', maskG)
	
	cv2.imshow('resB',res_blue)
	cv2.imshow('resG',res_green)
	
	k = cv2.waitKey(1) & 0xFF
	key = cv2.waitKey(1) & 0xFF
	if k == ord("q"): 
		count +=1	
	
	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	#count +=1
	#done = time.time() - t
	
	if (count == 100):
		break
	#if key == ord("q"):
		#break
camera.close()
done = time.time() - t
print('time taken: ' + str(done))
