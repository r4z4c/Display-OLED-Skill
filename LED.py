
# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

import time, datetime, threading

# Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos * 3, 0)
# pixels.count()
# pixels.set_pixel(i, wheel(((i * 256 // pixels.count())) % 256) )
# pixels.show()
# pixels.clear()
# pixels.get_pixel_rgb(i)
# reversed(range(i, pixels.count()))

class showTime:

    # Configure the count of pixels:
    PIXEL_COUNT = 24

    # Alternatively specify a hardware SPI connection on /dev/spidev0.0:
    SPI_PORT   = 0
    SPI_DEVICE = 0
    pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

    comparesecond = 0
    t = 0

    config = {'state': None, 'brightness': None, 'show': None, 'r': None, 'g': None, 'b': None}

    def __init__(self):
        with open('settings.json', 'r') as json_file:
            data = json.load(json_file)
            self.config['state'] = boolean(data['LED']['state'])
            self.config['brightness'] = float(data['LED']['brightness'])
            self.config['show'] = char(data['LED']['show'])
            self.config['r'] = int(data['LED']['r'])
            self.config['g'] = int(data['LED']['g'])
            self.config['b'] = int(data['LED']['b'])

    def config_led(config = {'state': None, 'brightness': None, 'show': None, 'r': None, 'g': None, 'b': None}):
        for c in self.config:
            if config[c] is not None:
                self.config[c] = config[c]


    def set_leds(self, number):
        highnumber = number/10
        lownumber = number%10

        leds = [[0, 0, 0, 0],[0, 0, 0, 0]]

        leds[0][0] = highnumber/8
        leds[0][1] = highnumber%8/4
        leds[0][2] = highnumber%8%4/2
        leds[0][3] = highnumber%8%4%2/1

        leds[1][3] = lownumber/8
        leds[1][2] = lownumber%8/4
        leds[1][1] = lownumber%8%4/2
        leds[1][0] = lownumber%8%4%2/1

        return leds

    def show_time(self, r, g, b, brightness):
        self.comparesecond
        currentsecond = datetime.datetime.now().second
        while(currentsecond == self.comparesecond):
            currentsecond = datetime.datetime.now().second

        comparesecond = datetime.datetime.now().second

        now = datetime.datetime.now()

        nowtime = {now.hour, now.minute, now.second}

        for k in nowtime:
            leds = self.set_leds(k)

            for i in range(len(leds)):
                for j in range(len(leds[i])):
                    if leds[i][j] == 1:
                        self.pixels.set_pixel(j+(k*i*4), Adafruit_WS2801.RGB_to_color(int(r*brightness), int(g*brightness), int(b*brightness)))
                    else:
                        self.pixels.set_pixel(j+(k*i*4), Adafruit_WS2801.RGB_to_color(0, 0, 0))

        self.pixels.show()

        def show_date(self, r, g, b, brightness):
            now = datetime.datetime.now()

            nowdate = {now.year, now.month, now.day}

            for k in nowtime:
                leds = self.set_leds(k)

                for i in range(len(leds)):
                    for j in range(len(leds[i])):
                        if leds[i][j] == 1:
                            self.pixels.set_pixel(j+(k*i*4), Adafruit_WS2801.RGB_to_color(int(r*brightness), int(g*brightness), int(b*brightness)))
                        else:
                            self.pixels.set_pixel(j+(k*i*4), Adafruit_WS2801.RGB_to_color(0, 0, 0))

            self.pixels.show()

        def run(self):
            self.pixels.clear()
            self.pixels.show()

            while True:
                if self.config["state"]:
                    if self.config['show']:
                        self.show_date(self.config['r'],self.config['g'], self.config['b'], self.config['brightness'])

                    if self.config['show']:
                        self.show_time(self.config['r'],self.config['g'], self.config['b'], self.config['brightness'])

        def close(self):
            for i in range(24):
                self.pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 0, 0))
            self.pixels.show()
