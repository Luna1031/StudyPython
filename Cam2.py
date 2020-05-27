import picamera

with picamera.PiCamera() as cam:
    cam.resolution = (640, 480)
    cam.start_preview()
    cam.start_recording('foo.h264')
    cam.wait_recording(60)
    cam.stop_recording()