#!/usr/bin/python
import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4,False)

with picamera.PiCamera() as camera:

	camera.resolution = (2592, 1944)
	camera.exif_tags['IFD0.Copyright'] = 'Eye-Pi Camera by P1X'
	camera.sharpness = 50
	camera.exposure_mode = 'night'
	camera.drc_strength = 'high'
	camera.annotate_text = 'Eye-Pi Camera by P1X'
	while True:
		GPIO.wait_for_edge(17, GPIO.FALLING)
		GPIO.output(4, True)
		ticks = time.time()
		camera.capture('/home/pi/cam/drop%03d.jpg' % ticks)
		GPIO.output(4, False)
