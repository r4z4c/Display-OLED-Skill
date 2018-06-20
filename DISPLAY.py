# coding=utf-8

import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import threading, json, sys, time
from os.path import dirname, abspath

sys.path.append(abspath(dirname(__file__)))

import TIME

a=u"°" # to display special strings

class theDisplay(threading.Thread):

    state = True

    myTime = None

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
    font = ImageFont.truetype("/opt/mycroft/skills/skill-my-alarm/font/arial.ttf", 12)
    font_b = ImageFont.truetype("/opt/mycroft/skills/skill-my-alarm/font/arial.ttf", 20)
    font_c = ImageFont.truetype("/opt/mycroft/skills/skill-my-alarm/font/arial.ttf", 14)

    config = {'status': None, 'show': None}

    json_file = "/opt/mycroft/skills/skill-my-alarm/settings.json"

    def __init__(self):
        threading.Thread.__init__(self)
        self.myTime = TIME.theTime()

        with open(self.json_file, 'r') as file:
            data = json.load(file)
            DISPLAY = data['DISPLAY']
            self.config['status'] = DISPLAY['status']
            self.config['show'] = DISPLAY['show']

        self.name = "myDisplay"

        self.disp.begin()
        self.disp.clear()
        self.disp.display()

        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)
        # Write one line of text.
        self.draw.text((self.x, self.top+25), 'Initializing...', font=self.font_c, fill=255)
        self.disp.image(self.image)
        self.disp.display()

    def run(self):
        while True:
            while self.config['status']:
                if self.config['show'] == "off":
                    self.disp.clear()
                    self.disp.display()
                    while self.config['show'] == "off":
                        pass

                elif self.config['show'] == "on":
                    while self.config['show'] == "on":
                        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0) #clear display
                        displayTime = self.myTime.textTime()
                        self.draw.text((self.x+37, self.top+10), displayTime, font=self.font_b, fill=255)
                        self.draw.line((self.x, self.top+32, self.x+self.width, self.top+32), fill=255)
                        displayDate = self.myTime.textDate()
                        self.draw.text((self.x+12, self.top+34), displayDate, font=self.font_b, fill=255)
                        self.disp.image(self.image)
                        self.disp.display()
                        time.sleep(0.1)

    def stop(self):
        self.disp.clear()
        self.disp.display()
