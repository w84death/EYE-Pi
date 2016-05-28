#
# EYE-Pi Camera Software
#
# Krzysztof Jankowski
# (c) 2016 P1X
#
# source: https://github.com/w84death/EYE-Pi 
# www: http://p1x.in


# Import stuff
import time
import picamera
import RPi.GPIO as GPIO

camera_loop = True
PIN_LED = 4
PIN_BUTTON_A = 17
PIN_BUTTON_POWER = 27
#PIN_SWITCH_ISO = 22

busy = False

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
chan_list = [PIN_BUTTON_A, PIN_BUTTON_POWER]
GPIO.setup(chan_list, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(PIN_LED, GPIO.OUT)

# Dim the LED
GPIO.output(PIN_LED, False)

# Init events
GPIO.add_event_detect(PIN_BUTTON_A, GPIO.FALLING)
GPIO.add_event_detect(PIN_BUTTON_POWER, GPIO.FALLING)


def killpi():
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output


# Run camera module
with picamera.PiCamera() as camera:

	# setup camera
	camera.resolution = (2592, 1944) # max for 5MPix module
 	camera.exif_tags['IFD0.Copyright'] = 'EYE-Pi Camera by P1X'
	camera.sharpness = 50
	camera.exposure_mode = 'antishake'
	camera.annotate_text = 'EYE-Pi Camera by P1X'

	# ready to shoot
	while camera_loop:
		if GPIO.event_detected(PIN_BUTTON_A) and !busy:
			busy = True
			GPIO.output(PIN_LED, True)
			ticks = time.time()
			camera.capture('/media/usb/eyepi-%03d.jpg' % ticks)
			GPIO.output(PIN_LED, False)
			busy = False
		if GPIO.event_detected(PIN_BUTTON_POWER):
			busy = True
			GPIO.output(PIN_LED, True)
			GPIO.remove_event_detect(PIN_BUTTON_A)
			#GPIO.cleanup()
			camera_loop = False
			killpi() #SYSTEM SHUTDOWN
