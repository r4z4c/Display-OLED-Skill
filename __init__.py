
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
import threading, sys, time, os
from os.path import dirname, abspath
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message
import RPi.GPIO as GPIO
from subprocess import call

sys.path.append(abspath(dirname(__file__)))

import LED, DISPLAY

import RPi.GPIO as GPIO

__author__ = 'uffi'

LOGGER = getLogger(__name__)

class DisplayOLEDSkill(MycroftSkill):

    myLEDs = None
    myDisplay = None

    messagebusClient = WebsocketClient()

    pin1 = 17
    pin2 = 27
    pin3 = 22

    def __init__(self):
        super(DisplayOLEDSkill, self).__init__(name="DisplayOLEDSkill")
        self.myLEDs = LED.theLEDs()
        self.myDisplay = DISPLAY.theDisplay()
        self.myLEDs.start()
        self.myDisplay.start()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin1, GPIO.RISING, callback=self.button_shutdown)
        GPIO.add_event_detect(self.pin2, GPIO.RISING, callback=self.button_stop_alarm)
        GPIO.add_event_detect(self.pin3, GPIO.RISING, callback=self.button_stop_alarm)

    def onConnected(self, event=None):
        self.messagebusClient.emit(Message("recognizer_loop:utterance",data={'utterances': 'cancel alarm'}))
        self.messagebusClient.close()

    def button_shutdown(self, channel):
        self.myDisplay.config['show'] = 'off'
        self.myLEDs.config['show'] = 'off'
        time.sleep(1)
        command = "/usr/bin/sudo /sbin/shutdown now"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]

    def button_stop_alarm(self, channel):
        while GPIO.input(self.pin2) or GPIO.input(self.pin3):
            if GPIO.input(self.pin2) and GPIO.input(self.pin3):
                self.messagebusClient.on('connected', self.onConnected)
                time.sleep(1)
                break

    @intent_handler(IntentBuilder("AllOffIntent").require("AllOff"))
    def handle_turn_all_off_intent(self, message):
        self.myDisplay.config['show'] = 'off'
        self.myLEDs.config['show'] = 'off'

    @intent_handler(IntentBuilder("TurnDisplayOnIntent").require("TurnDisplayOn"))
    def handle_turn_display_on_intent(self, message):
        self.myDisplay.config['show'] = 'on'

    @intent_handler(IntentBuilder("TurnDisplayOffIntent").require("TurnDisplayOff"))
    def handle_turn_display_off_intent(self, message):
        self.myDisplay.config['show'] = 'off'

    @intent_handler(IntentBuilder("TurnLightOnIntent").require("TurnLightOn"))
    def handle_turn_light_on_intent(self, message):
        self.myLEDs.config['show'] = 'light'

    @intent_handler(IntentBuilder("TurnLEDsOffIntent").require("TurnLEDsOff"))
    def handle_turn_leds_off_intent(self, message):
        self.myLEDs.config['show'] = 'off'

    @intent_handler(IntentBuilder("ShowDateIntent").require("ShowDate"))
    def handle_Show_date_intent(self, message):
        self.myLEDs.config['show'] = 'date'


    @intent_handler(IntentBuilder("ShowTimeIntent").require("ShowTime"))
    def handle_show_time_intent(self, message):
        self.myLEDs.config['show'] = 'time'

    @intent_handler(IntentBuilder("BrightnessUpIntent").require("BrightnessUp"))
    def brightness_up_intent(self, message):
        self.myLEDs.config['brightness'] += 0.3
        if self.myLEDs.config['brightness'] > 1:
            self.myLEDs.config['brightness'] = 1

    @intent_handler(IntentBuilder("BrightnessDownIntent").require("BrightnessDown"))
    def brightness_up_intent(self, message):
        self.myLEDs.config['brightness'] -= 0.3
        if self.myLEDs.config['brightness'] < 0.1:
            self.myLEDs.config['brightness'] = 0.1

    def stop(self):
        self.myDisplay.config['show'] = 'off'
        self.myLEDs.config['show'] = 'off'


def create_skill():
    return DisplayOLEDSkill()
