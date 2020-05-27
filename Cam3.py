import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1200, 720)
    camera.start_preview()
    camera.exposure_compensation = 2
    camera.exposure_mode = 'auto'
    camera.meter_mode = 'matrix'
    camera.image_effect = 'sketch'

    time.sleep(10)
    camera.exif_tags['IFD0.Artist'] = 'Lee'
    camera.exif_tags['IFD0.Copyrigth'] = 'Lee'
    camera.capture('foo.jpg')
    camera.stop_prev()