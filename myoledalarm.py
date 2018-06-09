#!/usr/bin/python

# this is my script for my alarm to handle the oled display

import RPi.GPIO as GPIO
import sys, os, time, datetime, jason

import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

a=u"°" # to display special strings
 
Display_on = True

class handleOLED():
  def __init__(self):
    super(handleOLED, self).__init__(name="handleOLED")
    
  def currentTime(stringa, stringb):
    now = datetime.datetime.now()
    nowyear = now.year
    nowmonth = now.month
    nowday = now.day
    nowhour = now.hour
    nowminute = now.minute
    nowsecond = now.second
    nowTime = str(nowhour).zfill(2) + ":" + str(nowminute).zfill(2) + ":" + str(nowsecond).zfill(2)
    nowDate = str(nowday).zfill(2) + "." + str(nowmonth).zfill(2) + "." + str(nowyear)
    if stringa == "time" and stringb == "date":
      theTime = nowTime + " " + nowDate
    elif stringa == "date" and stringb == "time":
      theTime = nowDate + " " + nowTime
    elif stringa == "time" and stringb == "":
      theTime = nowTime
    elif stringa == "date" and stringb == "":
      theTime = nowDate
    else:
      theTime = now
    return theTime

RST = 24
 
# Display 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
 
# Initialize library.
disp.begin()
 
# Clear display.
disp.clear()
disp.display()
 
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
 
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
 
# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
 
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = height-padding
 
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
 
# Load default font.
# font = ImageFont.load_default() # Wenn keine eigene Schrift vorhanden ist!!!! 
font = ImageFont.truetype("font/arial.ttf", 12) # Schriftart, Schriftgröße
font_b = ImageFont.truetype("font/arial.ttf", 18)
font_c = ImageFont.truetype("font/arial.ttf", 14)
 
# Write one line of text.
draw.text((x, top+25), 'Start', font=font_b, fill=255)
 
# Display image.
disp.image(image)
disp.display()
 
oled = handleOLED()
  
# mainroutine
#-------------------------------- 

while Display_on:
  draw.rectangle((0,0,width,height), outline=0, fill=0) #clear display
  displayTime = oled.currentTime("time", "date") 
  draw.line((x, top+48, x+width, top+48), fill=255)
  draw.text((x, top+50), displayTime, font=font, fill=255)
  disp.image(image)
  disp.display()
