
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
import threading, sys, time
from os.path import dirname, abspath

#sys.path.append(abspath(dirname(__file__)))
#import MAINPY
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)

__author__ = 'usia'

LOGGER = getLogger(__name__)

class myThread(threading.Thread):

  count = 10

  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    while self.count > 0:
      if self.count%2:
        GPIO.output(22, GPIO.HIGH)
      else:
        GPIO.output(22, GPIO.LOW)
      time.sleep(2)
      self.count = self.count-1

class DisplayOLEDSkill(MycroftSkill):

  def __init__(self):
    super(DisplayOLEDSkill, self).__init__(name="DisplayOLEDSkill")    

  @intent_handler(IntentBuilder("ShowOnDisplayIntent").require("ShowOnDisplayKeyword"))
  def handle_show_on_display_intent(self, message):
    self.speak_dialog("is.okay")

  def stop(self):
    pass

def create_skill():
  theThread = myThread()
  theThread.start()
  return DisplayOLEDSkill()
