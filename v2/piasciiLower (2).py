import serial
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from string import ascii_lowercase

ser = serial.Serial('/dev/ttyACM0')

camera = PiCamera()
camera.resolution = (640, 480)
camera.shutter_speed = 2000
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))
j = 0
time.sleep(0.5)
for i in 'qwertyuiopasdfgh':
  ser.write(i)
  print(i)
  xx = "{0:b}".format(j).zfill(4)
  j = j+1
  time.sleep(0.5)
  camera.capture('/home/pi/Desktop/Images2/%s.jpg' %xx)
  time.sleep(0.5)

