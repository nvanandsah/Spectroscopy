from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 

camera = PiCamera()
camera.resolution = (640, 480)
camera.shutter_speed = 2200
camera.framerate = 60
#camera.exposure = 0
rawCapture = PiRGBArray(camera, size=(640, 480))
#rawCapture = PiRGBArray(camera)
count = 0
t = time.time()

time.sleep(0.5)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	img = frame.array
	#cv2.imshow("response", image)
	cv2.imwrite("pictures/frame" + str(count) + ".jpg", img)
	
	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	count +=1
	#done = time.time() - t
	
	if (count == 5):
		break
	#if key == ord("q"):
		#break
camera.close()
done = time.time() - t
print('time taken: ' + str(done))
