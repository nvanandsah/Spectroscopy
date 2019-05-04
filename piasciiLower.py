import serial
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from string import ascii_lowercase

ser = serial.Serial('/dev/ttyACM0')

camera = PiCamera()
camera.resolution = (640, 480)
camera.shutter_speed = 1000
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))
camera.start_preview()
for i in ascii_lowercase:
  ser.write(i)
  print(i)
  camera.capture('/home/pi/Desktop/Images/%s.jpg' %i)
  time.sleep(0.1)
k='a'
ser.write(k)
print(k)
camera.capture('/home/pi/Desktop/Images/a.jpg')
camera.stop_preview()





































