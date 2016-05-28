import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

disp = Adafruit_SSD1306.SSD1306_128_64(rst=24, i2c_address=0x3D)
disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.open('test.jpg')
image_small = image.resize((width,height), Image.BICUBIC)
image_oled = image_small.convert("1")

#draw = ImageDraw.Draw(image_oled)
#font = ImageFont.load_default()
#draw.text((0, 0), 'EYE-Pi Camera',  font=font, fill=255)

disp.image(image_oled)
disp.display()

