import cv2
from PIL import Image
from imutils import contours
import imutils
from skimage import measure
import numpy as np
import time
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import tree

start = time.time()
r1 =[]
r2=[]
val1 = []
val2 = []
Y = []
for iii in range(16):
    xx = "{0:b}".format(iii).zfill(4)
    #print(xx)
    img = cv2.imread('c4/%s.jpg' %xx, flags=cv2.IMREAD_COLOR)
    Y.append(xx)
    firstpart, secondpart = xx[:int(len(xx)/2)], xx[int(len(xx)/2):]
    val1.append(firstpart)
    val2.append(secondpart)
    lower_red = np.array([0,50,50]) 
    upper_red = np.array([10,255,255]) 

    lower_red2 = np.array([165,50,50]) 
    upper_red2 = np.array([180,255,255])
    mask = []
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    maskR = cv2.inRange(hsv, lower_red, upper_red)
    maskR2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask.append(maskR+maskR2)
    lower_green = np.array([44,50,50])
    upper_green = np.array([70,255,255])
    maskG = cv2.inRange(hsv,lower_green, upper_green)
    mask.append(maskG)

    lower_blue = np.array([105,50,50])
    upper_blue = np.array([127,255,255])
    maskB = cv2.inRange(hsv,lower_blue,upper_blue)
    lower_yellow = np.array([50,255,255])
    upper_yellow = np.array([65,255,255])
    maskY = cv2.inRange(hsv,lower_yellow,upper_yellow)
    mask = np.array(mask)
    for colorx in range(2):
        img1 = mask[colorx,:,:]

        kernel = np.ones((5,5),np.uint8)
        blurred=cv2.GaussianBlur(img1,(11,11),0)
        threshold=cv2.threshold(blurred,200,255,cv2.THRESH_BINARY)[1]
        #threshold=cv2.erode(threshold,np.ones((1,1),np.uint8),iterations=1)
        threshold=cv2.dilate(threshold,np.ones((10,10),np.uint8),iterations=2)
        #cv2.imshow("image4",threshold)
        #cv2.waitKey(0)
        try:
            major = cv2.__version__.split('.')[0]
            if major == '3':
                _, con, _ = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            else:
                con, _ = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cons=contours.sort_contours(con)[0]
            for(i,c) in enumerate(cons):
                    (x,y,w,h)=cv2.boundingRect(c)
                    #crop=masked_data[y:y+h,x:x+w]
                    ((cx,cy),radius)=cv2.minEnclosingCircle(c)
                    crop=cv2.circle(img,(int(cx),int(cy)),int(radius),(200,0,255),1)
                    #print(colorx,"  ",colorx,",",radius)
                    if(colorx==0):
                        r1.append("{0:.2f}".format(radius))
                    else:
                        r2.append("{0:.2f}".format(radius))
        except:
                pass
        #cv2.imshow("image1",img)
        #cv2.waitKey(0)
print("time taken ", time.time()-start)
print("\n")
print(r1)
print(r2)
print("\n")
X1 = np.array(r1).reshape(-1,1)
Y1 = np.array(val1).reshape(-1,1)
X2 = np.array(r2).reshape(-1,1)
Y2 = np.array(val2).reshape(-1,1)
clf1 = DecisionTreeClassifier()
clf1 = clf1.fit(X1,Y1)
clf2 = DecisionTreeClassifier()
clf2 = clf2.fit(X2,Y2)


r1 = []
r2 = []
Y1 = []
for iii in range(16):
    xx = "{0:b}".format(iii).zfill(4)
    #print(xx)
    img = cv2.imread('2/%s.jpg' %xx, flags=cv2.IMREAD_COLOR)
    Y1.append(xx)
    lower_red = np.array([0,50,50]) 
    upper_red = np.array([10,255,255]) 

    lower_red2 = np.array([165,50,50]) 
    upper_red2 = np.array([180,255,255])
    mask = []
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    maskR = cv2.inRange(hsv, lower_red, upper_red)
    maskR2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask.append(maskR+maskR2)
    #cv2.imshow("maskR",cv2.bitwise_and(img, img, mask = maskR + maskR2))
    #cv2.waitKey(0)
    lower_green = np.array([44,50,50])
    upper_green = np.array([70,255,255])
    maskG = cv2.inRange(hsv,lower_green, upper_green)
    mask.append(maskG)

    lower_blue = np.array([105,50,50])
    upper_blue = np.array([127,255,255])
    maskB = cv2.inRange(hsv,lower_blue,upper_blue)
    mask = np.array(mask)
    for colorx in range(2):
        img1 = mask[colorx,:,:]

        kernel = np.ones((5,5),np.uint8)
        blurred=cv2.GaussianBlur(img1,(11,11),0)
        threshold=cv2.threshold(blurred,200,255,cv2.THRESH_BINARY)[1]
        #threshold=cv2.erode(threshold,np.ones((1,1),np.uint8),iterations=1)
        threshold=cv2.dilate(threshold,np.ones((10,10),np.uint8),iterations=2)
        #cv2.imshow("image4",threshold)
        #cv2.waitKey(0)
        try:
            major = cv2.__version__.split('.')[0]
            if major == '3':
                _, con, _ = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            else:
                con, _ = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cons=contours.sort_contours(con)[0]
            for(i,c) in enumerate(cons):
                    (x,y,w,h)=cv2.boundingRect(c)
                    #crop=masked_data[y:y+h,x:x+w]
                    ((cx,cy),radius)=cv2.minEnclosingCircle(c)
                    crop=cv2.circle(img,(int(cx),int(cy)),int(radius),(200,0,255),1)
                    #print(colorx,"  ",colorx,",",radius)
                    if(colorx==0):
                        r1.append("{0:.2f}".format(radius))
                    else:
                        r2.append("{0:.2f}".format(radius))
        except:
                pass
print("\n")
print(r1)
print(r2)
print("\n")
r1 = np.array(r1).reshape(-1,1)
r2 = np.array(r2).reshape(-1,1)
y_pred1 = clf1.predict(r1)
y_pred2 = clf2.predict(r2)
y_pred = [y_pred1[i]+y_pred2[i] for i in range(len(y_pred2))]
print(y_pred)
print("Accuracy:",accuracy_score(Y1, y_pred))
