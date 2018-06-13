
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
import threading, sys, time
from os.path import dirname, abspath

sys.path.append(abspath(dirname(__file__)))

import RPi.GPIO as GPIO

__author__ = 'uffi'

LOGGER = getLogger(__name__)


class myThread(threading.Thread):

    

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        pass

class DisplayOLEDSkill(MycroftSkill):

    def __init__(self):
        super(DisplayOLEDSkill, self).__init__(name="DisplayOLEDSkill")

    @intent_handler(IntentBuilder("ShowOnDisplayIntent").require("ShowOnDisplayKeyword"))
    def handle_show_on_display_intent(self, message):
        self.speak_dialog("is.okay")

    def stop(self):
        pass

def create_skill():
    #theThread = myThread()
    #theThread.start()
    return DisplayOLEDSkill()
