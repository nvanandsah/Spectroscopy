import cv2
import numpy
count = 0
while (count < 100):
	img = cv2.imread("pictures/frame"+str(count)+".jpg", flags=cv2.IMREAD_COLOR)	
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

  
# Destroys all of the HighGUI windows. 
cv2.destroyAllWindows() 
  
# release the captured frame 

 
