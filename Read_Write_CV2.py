import numpy as np
import cv2
import imutils
import datetime
stream = cv2.VideoCapture(0)
s = datetime.datetime.now()
n = ''
i = 0
while i < 100:
	(grabbed, frame) = stream.read()
	frame = cv2.resize(frame, (32,32), interpolation = cv2.INTER_CUBIC)
	n = 'Recieved/'+datetime.datetime.now().strftime("%H%M%S%f")+'.bmp'
	#cv2.imwrite(n,frame)
	i = i+1
	print(n)
end = datetime.datetime.now()
print("Time taken "+str((end-s).total_seconds()))
stream.release()
cv2.destroyAl
Windows()