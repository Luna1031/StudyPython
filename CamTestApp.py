import time
import picamera

camera = picamera.PiCamera()

try:
    camera.start_preview()
    time.sleep(10)
    camera.stop_preview()
finally:
    camera.close()

# with picamera.PiCamera() as camera:
#     camera.start_preview()
#     time.sleep(10)
#     camera.stop_preview()