
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
import threading, sys, time
from os.path import dirname, abspath

sys.path.append(abspath(dirname(__file__)))

import LED, DISPLAY

import RPi.GPIO as GPIO

__author__ = 'uffi'

LOGGER = getLogger(__name__)

class DisplayOLEDSkill(MycroftSkill):

    myLEDs = None
    myDisplay = None

    def __init__(self):
        super(DisplayOLEDSkill, self).__init__(name="DisplayOLEDSkill")
        self.myLEDs = LED.theLEDs()
        #self.myDisplay = DISPLAY.theDisplay()
        self.myLEDs.start()
        #self.myDisplay.start()

    @intent_handler(IntentBuilder("AllOffIntent").require("AllOffKeyword"))
    def handle_turn_all_off_intent(self, message):
        pass

    @intent_handler(IntentBuilder("TurnDisplayOnIntent").require("TurnDisplayOn"))
    def handle_turn_display_on_intent(self, message):
        pass
    @intent_handler(IntentBuilder("TurnDisplayOffIntent").require("TurnDisplayOff"))
    def handle_turn_display_off_intent(self, message):
        pass

    @intent_handler(IntentBuilder("TurnLightOnIntent").require("TurnLightOn"))
    def handle_turn_light_on_intent(self, message):
        self.myLEDs.config['show'] = 'on'

    @intent_handler(IntentBuilder("TurnLEDsOffIntent").require("TurnLEDsOff"))
    def handle_turn_leds_off_intent(self, message):
        self.myLEDs.config['show'] = 'off'

    @intent_handler(IntentBuilder("ShowDateIntent").require("ShowDate"))
    def handle_Show_date_intent(self, message):
        self.myLEDs.config['show'] = 'date'


    @intent_handler(IntentBuilder("ShowTimeIntent").require("ShowTime"))
    def handle_show_time_intent(self, message):
        self.myLEDs.config['show'] = 'time'


    def stop(self):
        pass

def create_skill():
    return DisplayOLEDSkill()
