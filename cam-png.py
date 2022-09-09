from picamera import PiCamera
from time import sleep
file_name = input('Enter file name: ' )
file_path = '/home/ncaravias/label-printer/' + file_name + '.png'

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture(file_path)
camera.stop_preview()

