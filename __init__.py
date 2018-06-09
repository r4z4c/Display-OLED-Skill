
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
import threading, sys
from os.path import dirname, abspath

#sys.path.append(abspath(dirname(__file__)))
#import MAINPY
import RPi.GPIO as GPIO

__author__ = 'usia'

LOGGER = getLogger(__name__)

class myThread(threading.Thread):

  count = 10

  def __init__(self):
    threading.Thread.__init__(self)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.OUT)

  def run(self):
    while count > 0:
      if count%2:
        GPIO.output(22, GPIO.HIGH)
      else:
        GPIO.output(22, GPIO.LOW)
	
      count = count-1

class DisplayOLEDSkill(MycroftSkill):

  def __init__(self):
    super(DisplayOLEDSkill, self).__init__(name="DisplayOLEDSkill")

    theThread = myThread()
    theTread.start()

  @intent_handler(IntentBuilder("ShowOnDisplayIntent").require("ShowOnDisplayKeyword"))
  def handle_show_on_display_intent(self, message):
    self.speak_dialog("is.okay")

  def stop(self):
    pass

def create_skill():
	return DisplayOLEDSkill()
