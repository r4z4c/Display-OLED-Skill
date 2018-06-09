# coding=utf-8

import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont

a=u"°" # to display special strings


class ShowOnDisplay():
  
  disp_on = True

  # Raspberry Pi pin configuration:
  RST = 24
  
  disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
  
  width = disp.width
  height = disp.height
  image = Image.new('1', (width, height))
  
  draw = ImageDraw.Draw(image)
  
  padding = 2
  shape_width = 20
  top = padding
  bottom = height-padding
  
  x = padding
  
  font_default = ImageFont.load_default()
  font = ImageFont.truetype("arial.ttf", 12)
  font_b = ImageFont.truetype("arial.ttf", 18)
  font_c = ImageFont.truetype("arial.ttf", 14)
  
  
  def __init__(self):
    self.name = "ShowOnDisplay"
    
    self.disp.begin()
    self.disp.clear()
    self.disp.display()
    
    self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
    # Write one line of text.
    self.draw.text((self.x, self.top+25), 'Initializing...', self.font_default, fill=255)
    self.disp.image(image)
    self.disp.display()
    
  def reset(self):
    self.disp.clear()
    self.disp.display()

def create():
  return ShowOnDisplay()
