#
# EYE-Pi Camera Software
# Ver. 2.1 (OLED)
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
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Const and vars

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
GPIO.output(PIN_LED, False)

# Setup OLED
disp = Adafruit_SSD1306.SSD1306_128_64(rst=24, i2c_address=0x3D)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height


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
		if GPIO.event_detected(PIN_BUTTON_A) and not busy:
			busy = True
			GPIO.output(PIN_LED, True)
			camera.resolution = (2592, 1944)
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

		camera.resolution = (640, 480)
		camera.capture('oled.jpg')
		image = Image.open('oled.jpg')
		image_small = image.resize((64,48), Image.BICUBIC)
		image_oled = image_small.convert("1")
		disp.image(image_oled)
		disp.display()
