
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
        self.myDisplay = DISPLAY.theDisplay()
        self.myLEDs.start()
        self.myDisplay.start()

    @intent_handler(IntentBuilder("TurnAllOffIntent").require("TurnAllOffKeyword"))
    def handle_turn_all_off_intent(self, message):

    @intent_handler(IntentBuilder("TurnDisplayOnIntent").require("TurnDisplayOnKeyword"))
    def handle_turn_display_on_intent(self, message):

    @intent_handler(IntentBuilder("TurnDisplayOffIntent").require("TurnDisplayOffKeyword"))
    def handle_turn_display_off_intent(self, message):


    @intent_handler(IntentBuilder("TurnLightOnIntent").require("TurnLightOnKeyword"))
    def handle_turn_light_on_intent(self, message):
        self.myLEDs.config['show'] = 'on'

    @intent_handler(IntentBuilder("TurnLEDsOffIntent").require("TurnLEDsOFFKeyword"))
    def handle_turn_leds_off_intent(self, message):
        self.myLEDs.config['show'] = 'off'

    @intent_handler(IntentBuilder("ShowDateIntent").require("ShowDateKeyword"))
    def handle_Show_date_intent(self, message):
        self.myLEDs.config['show'] = 'date'

    @intent_handler(IntentBuilder("ShowTimeIntent").require("ShowTimeKeyword"))
    def handle_show_time_intent(self, message):
        self.myLEDs.config['show'] = 'time'

    def stop(self):
        pass

def create_skill():
    return DisplayOLEDSkill()
