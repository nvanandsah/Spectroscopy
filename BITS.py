import cv2, collections
import numpy

for steps in range(2):
	inu = input("choose image ")

	img = cv2.imread("pictures/frame"+str(inu)+".jpg", flags=cv2.IMREAD_COLOR)

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
	countGre = 0	
	maskG = cv2.inRange(hsv,lower_green, upper_green)

	countRed = 0

	lower_blue = numpy.array([105,50,50])
	upper_blue = numpy.array([127,255,255])

	maskB = cv2.inRange(hsv,lower_blue,upper_blue)

	countBlu = 0


	for c in range(len(maskRED)):
		for ran in range(len(maskRED[c])):
			if(maskRED[c][ran] == 255):
				countRed+=1
				break
		if (countRed == 1):
			break
				
			#if(maskG[c][ran] == 255):
			#	countGre+=1
			

	#res_red = cv2.bitwise_and(img,img, mask = maskR) 
	#res2_red = cv2.bitwise_and(img,img,mask = maskR2)

	#resRED = res_red + res2_red



	for c2 in range(len(maskG)):
		for ran2 in range(len(maskG[c2])):
			if(maskG[c2][ran2] == 255):
				countGre+=1
				break
		if (countGre == 1):
			break
			
	for c3 in range(len(maskB)):
		for ran3 in range(len(maskB[c3])):
			if(maskB[c3][ran3] == 255):
				countBlu+=1
				break
		if (countBlu == 1):
			break

	print("green pixels: " + str(countGre))
	print("red pixels: " + str(countRed))
	print("blue pixels: " + str(countBlu))
	#res_green = cv2.bitwise_and(img,img, mask = maskG)
