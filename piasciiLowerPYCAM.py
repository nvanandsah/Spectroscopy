from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 

camera = PiCamera()
camera.resolution = (640, 480)
camera.shutter_speed = 1000
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(640, 480))
#rawCapture = PiRGBArray(camera)
count = 0
t = time.time()

time.sleep(0.1)
i=0
starttime = time.time()
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  img = frame.array
  #print(i)
  #XX = '/home/pi/Desktop/Images1/' + str(i).zfill(2) + '_1.jpg'
  #cv2.imwrite(XX,img)
  #print(i)
  #XX = '/home/pi/Desktop/Images1/' + str(i).zfill(2) + '_2.jpg'
  #cv2.imwrite(XX,img)
  #print(i)
  #XX = '/home/pi/Desktop/Images1/' + str(i).zfill(2) + '_3.jpg'
  #cv2.imwrite(XX,img)
  print(i)
  XX = '/home/pi/Desktop/Images1/' + str(i).zfill(2) + '_4.jpg'
  cv2.imwrite(XX,img)
  rawCapture.truncate(0)
  if(i<64):
    i = i+1
  else:
    break;
print("time taken in seconds %s seconds" %(time.time() - starttime))
