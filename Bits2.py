import cv2, collections
import numpy

for i in range(16):
	xx = "{0:b}".format(i).zfill(4)
	#inu = '/home/pi/Desktop/Images2/%s.jpg' %xx

	img = cv2.imread('/home/pi/Desktop/Images2/%s.jpg' %xx, flags=cv2.IMREAD_COLOR)

	lower_red = numpy.array([0,50,50]) 
	upper_red = numpy.array([10,255,255]) 

	lower_red2 = numpy.array([165,50,50]) 
	upper_red2 = numpy.array([180,255,255])

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	maskR = cv2.inRange(hsv, lower_red, upper_red)
	maskR2 = cv2.inRange(hsv, lower_red2, upper_red2)
	maskRED = maskR + maskR2

	lower_green = numpy.array([44,50,50])
	upper_green = numpy.array([70,255,255])
	maskG = cv2.inRange(hsv,lower_green, upper_green)



	lower_blue = numpy.array([105,50,50])
	upper_blue = numpy.array([127,255,255])
	maskB = cv2.inRange(hsv,lower_blue,upper_blue)


	threshold  = 1
	if (numpy.count_nonzero(maskRED==255) > threshold):
		CountR = 1
	else:
		CountR = 0
		
	if (numpy.count_nonzero(maskG==255) > threshold):
		CountG = 1
	else:
		CountG = 0
		
	if (numpy.count_nonzero(maskB==255) > threshold):
		CountB = 1
	else:
		CountB = 0
		
	#print(CountR)	
	#print(CountG)		
	#print(CountB)			
	print(xx)
	print("RED pixels: " + str(numpy.count_nonzero(maskRED==255)))
	print("GREEN pixels: " + str(numpy.count_nonzero(maskG==255)))
	print("DIFF pixels: " + str(numpy.count_nonzero(maskRED==255)-numpy.count_nonzero(maskG==255)))
