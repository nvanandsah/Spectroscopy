import serial
import time
import cv2
from string import ascii_lowercase
from picamera.array import PiRGBArray
from picamera import PiCamera

#ser = serial.Serial('/dev/ttyACM0')

#camera = cv2.VideoCapture(0)
#camera.set(15,0)
#camera.set(cv2.cv.CV_CAP_PROP_FPS,60)


camera = PiCamera()
camera.resolution = (640, 480)
camera.shutter_speed = 1000
camera.framerate = 60
rawCapture = PiRGBArray(camera, size=(640, 480))






time.sleep(0.1)

#_,frame = camera.capture()

for i in range(16):
  #camera.start_preview()
  starttime = time.time()
  ###time.sleep(0.15)
  print(i)
  #_,frame = camera.capture()
  XX = '/home/pi/Desktop/Images1/' + str(i).zfill(2) + '_1.jpg'
  camera.capture(XX)
  #cv2.imwrite(XX,frame)
  #time.sleep(0.15)
  print(i)
  #_,frame = camera.capture()
  XX = '/home/pi/Desktop/Images1/' + str(i).zfill(2) + '_2.jpg'
  camera.capture(XX)
  #cv2.imwrite(XX,frame)
  #time.sleep(0.15)
  print(i)
  #_,frame = camera.capture()
  XX = '/home/pi/Desktop/Images1/' + str(i).zfill(2) + '_3.jpg'
  camera.capture(XX)
  #cv2.imwrite(XX,frame)
  #time.sleep(0.15)
  print(i)
  # _,frame = camera.capture()
  XX = '/home/pi/Desktop/Images1/' + str(i).zfill(2) + '_4.jpg'
  camera.capture(XX)
  #cv2.imwrite(XX,frame)
  #time.sleep(0.15)
  print("time taken in seconds %s seconds" %(time.time() - starttime))
  #camera.stop_preview()
