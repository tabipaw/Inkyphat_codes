
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne
import ipget

#Get IP address of wlan0 (Raspberry pi wifi)
ipnum = ipget.ipget()
ipstr = ipnum.ipaddr("wlan0") 

#Set screen params
inky_display = InkyPHAT("yellow")
inky_display.set_border(inky_display.WHITE)
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(FredokaOne, 22)
message = "SSH me, if you can!\n" + ipstr + " :)"
x = 10
y = 10

#write screen            
draw.text((x, y), message, inky_display.YELLOW, font)
inky_display.set_image(img)
inky_display.show()
