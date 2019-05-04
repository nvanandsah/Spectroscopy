import cv2, collections
import numpy
inu = input("choose image ")

img = cv2.imread("Images/"+str(inu)+".jpg", flags=cv2.IMREAD_COLOR)

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


lower_yellow = numpy.array([50,255,255])
upper_yellow = numpy.array([65,255,255])
maskY = cv2.inRange(hsv,lower_yellow,upper_yellow)




threshold  = 1
if (numpy.count_nonzero(maskRED==255) > threshold):
	CountR = "01"
else:
	CountR = 0
	
if (numpy.count_nonzero(maskG==255) > threshold):
	CountG = "10"
else:
	CountG = 0
	
if (numpy.count_nonzero(maskB==255) > threshold):
	CountB = "11"
else:
	CountB = 0
	
if (numpy.count_nonzero(maskY==255) > threshold):
	CountY = "00"
else:
	CountY = 0	
	
print(CountR)	
print(CountG)		
print(CountB)	
print(CountY)		

print("RED pixels: " + str(numpy.count_nonzero(maskRED==255)))
print("GREEN pixels: " + str(numpy.count_nonzero(maskG==255)))
print("BLUE pixels: " + str(numpy.count_nonzero(maskB==255)))
print("YELLOW pixels: " + str(numpy.count_nonzero(maskY==255)))
