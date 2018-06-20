
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
import threading, sys, time, os
from os.path import dirname, abspath
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message
import RPi.GPIO as GPIO

sys.path.append(abspath(dirname(__file__)))

import LED, DISPLAY

import RPi.GPIO as GPIO

__author__ = 'uffi'

LOGGER = getLogger(__name__)

class DisplayOLEDSkill(MycroftSkill):

    myLEDs = None
    myDisplay = None

    status = False

    messagebusClient = WebsocketClient()

    buttonEntry = None
    buttonHold = None
    bshutdown = 4
    brestart = 17
    bsleep1 = 27
    bsleep2 = 22

    def __init__(self):
        super(DisplayOLEDSkill, self).__init__(name="DisplayOLEDSkill")
        self.myLEDs = LED.theLEDs()
        self.myDisplay = DISPLAY.theDisplay()
        self.myLEDs.start()
        self.myDisplay.start()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bshutdown, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.brestart, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.bsleep1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.bsleep1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.bshutdown, GPIO.RISING, callback=self.button_shutdown)
        GPIO.add_event_detect(self.brestart, GPIO.RISING, callback=self.button_restart)
        GPIO.add_event_detect(self.bsleep1, GPIO.RISING, callback=self.button_stop_alarm)

    def onStopAlarm(self, event=None):
        self.messagebusClient.emit(Message("recognizer_loop:utterance",data={'utterances': ['cancel alarm']}))
        self.messagebusClient.close()
        time.sleep(0.5)

    def button_shutdown(self, channel):
        self.speak_dialog("shuttingdown")
        time.sleep(1)
        os.system("systemctl poweroff -i")

    def button_restart(self, channel):
        self.speak_dialog("restarting")
        time.sleep(1)
        os.system("systemctl reboot -i")

    def button_stop_alarm(self, channel):
        while GPIO.input(self.bsleep1):
            if GPIO.input(self.bsleep1) and GPIO.input(self.bsleep2):
                self.buttonEntry = time.time()
                while GPIO.input(self.bsleep1) and GPIO.input(self.bsleep2):
                    self.buttonHold = time.time()
                    if self.buttonHold-self.buttonEntry >= 1.5:
                        if self.status:
                            self.myLEDs.config['status'] = False
                            self.myDisplay.config['status'] = False
                            self.status = False
                        else:
                            self.myLEDs.config['status'] = True
                            self.myDisplay.config['status'] = True
                            self.status = True
                        break
                if self.buttonHold-self.buttonEntry < 1.5:
                    self.messagebusClient.on('connected', self.onStopAlarm)
                    self.myLEDs.config['show'] = 'light'
                break

    @intent_handler(IntentBuilder("AllOffIntent").require("AllOff"))
    def handle_turn_all_off_intent(self, message):
        self.myDisplay.config['show'] = 'off'
        self.myLEDs.config_led(self, config = {'status': None, 'brightness': None, 'show': 'off', 'r': None, 'g': None, 'b': None})

    @intent_handler(IntentBuilder("TurnDisplayOnIntent").require("TurnDisplayOn"))
    def handle_turn_display_on_intent(self, message):
        self.myDisplay.config['show'] = 'on'

    @intent_handler(IntentBuilder("TurnDisplayOffIntent").require("TurnDisplayOff"))
    def handle_turn_display_off_intent(self, message):
        self.myDisplay.config['show'] = 'off'

    @intent_handler(IntentBuilder("TurnLightOnIntent").require("TurnLightOn"))
    def handle_turn_light_on_intent(self, message):
        self.myLEDs.config_led(config = {'status': None, 'brightness': None, 'show': 'light', 'r': None, 'g': None, 'b': None})

    @intent_handler(IntentBuilder("TurnLEDsOffIntent").require("TurnLEDsOff"))
    def handle_turn_leds_off_intent(self, message):
        self.myLEDs.config_led(config = {'status': None, 'brightness': None, 'show': 'off', 'r': None, 'g': None, 'b': None})

    @intent_handler(IntentBuilder("ShowDateIntent").require("ShowDate"))
    def handle_Show_date_intent(self, message):
        self.myLEDs.config_led(config = {'status': None, 'brightness': None, 'show': 'date', 'r': None, 'g': None, 'b': None})

    @intent_handler(IntentBuilder("ShowTimeIntent").require("ShowTime"))
    def handle_show_time_intent(self, message):
        self.myLEDs.config_led(config = {'status': None, 'brightness': None, 'show': 'time', 'r': None, 'g': None, 'b': None})

    @intent_handler(IntentBuilder("BrightnessUpIntent").require("BrightnessUp"))
    def brightness_up_intent(self, message):
        brightness = self.myLEDs.config['brightness']
        if brightness == 0.025:
            brightness = 0.2
        elif brightness == 0.2:
            brightness = 0.6
        elif brightness == 0.6:
            brightness = 1
        else:
            brightness = 0.025

        config = {'status': None, 'brightness': brightness, 'show': None, 'r': None, 'g': None, 'b': None}
        self.myLEDs.config_led(config)

    @intent_handler(IntentBuilder("BrightnessDownIntent").require("BrightnessDown"))
    def brightness_down_intent(self, message):
        brightness = self.myLEDs.config['brightness']
        if brightness == 1:
            brightness = 0.6
        elif brightness == 0.6:
            brightness = 0.2
        else:
            brightness = 0.025

        config = {'status': None, 'brightness': brightness, 'show': None, 'r': None, 'g': None, 'b': None}
        self.myLEDs.config_led(config)

    @intent_file_handler('stop.intent')
    def _stop(self, message):
        """ Wrapper for stop method """
        self.stop()

    def stop(self):
        self.myDisplay.stop()
        self.myLEDs.stop()



def create_skill():
    return DisplayOLEDSkill()
