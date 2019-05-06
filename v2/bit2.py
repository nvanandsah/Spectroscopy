

1 of 20,994
plag
Inbox
x

KANHA SRIVASTAV
Attachments
1:41 PM (3 minutes ago)
to me


Attachments area

import cv2, collections
import numpy

storedR = []
storedG = []
for i in range(16):
        xx = "{0:b}".format(i).zfill(4)
        #inu = '/home/pi/Desktop/Images2/%s.jpg' %xx
        img = cv2.imread('Photos/4/%s.jpg' %xx, flags=cv2.IMREAD_COLOR)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        w = 639
        h = 479
        
        r1 = 0;
        c1 = 0;
        
        lower_red = numpy.array([0,50,50]) 
        upper_red = numpy.array([10,255,255]) 
        lower_red2 = numpy.array([165,50,50]) 
        upper_red2 = numpy.array([180,255,255])
        
        maskR = cv2.inRange(hsv, lower_red, upper_red)
        maskR2 = cv2.inRange(hsv, lower_red2, upper_red2)
        maskRED = maskR + maskR2
        lower_green = numpy.array([44,50,50])
        upper_green = numpy.array([70,255,255])
        maskG = cv2.inRange(hsv,lower_green, upper_green)

        cv2.imwrite('Photos/4/maskG/%s.jpg' %xx,maskG)
        cv2.imwrite('Photos/4/maskRED/%s.jpg' %xx,maskRED)

        #OnlyG = cv2.bitwise_and(img, img, mask = maskG)
        #OnlyR = cv2.bitwise_and(img, img, mask = maskRED)
        #print("here")
        print(xx)
        print("")

        #print("also here")
        for row2 in range(w):
                for col2 in range(h):
                        if(maskRED[col2][row2] == 255):
                                #print(col2)
                                break
                if(maskRED[col2][row2] == 255):
                        break

        #print("column2 " + str(col2))

        for row in range(w):
                for col in range(h):
                        if (maskG[col][w-row] == 255):
                                #print(col)
                                break

                if(maskG[col][w-row] == 255):
                        break
        
        #print("column1 " + str(col))
        #print("done")
        storedR.append(row2)
        storedG.append(w-row)
        
               
##        print(xx)
##        print("RED pixels: " + str(numpy.count_nonzero(maskRED==255)))
##        print("GREEN pixels: " + str(numpy.count_nonzero(maskG==255)))
##        print("DIFF pixels: " + str(numpy.count_nonzero(maskRED==255)-numpy.count_nonzero(maskG==255)))
##        print("ratio: " + str(numpy.count_nonzero(maskRED==255)/numpy.count_nonzero(maskG==255)))
##        print("")
print(storedR)
print(storedG)