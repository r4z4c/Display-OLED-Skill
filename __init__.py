
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
import threading, sys, time
from os.path import dirname, abspath

sys.path.append(abspath(dirname(__file__)))

import DISPLAY
import TIME

import RPi.GPIO as GPIO

mainmenu = [0, 0, 0, 0]

__author__ = 'usia'

LOGGER = getLogger(__name__)

class myDisplay:
  
  statechange = true
  
  bup = 17
  bdown = 27
  bleft = 22
  bright = 18
  bset = 23
  bmenu = 24
  bsnooze1 = 5
  bsnooze2 = 6
  
  menudepth = 0
  themenu = [[], [], [], [[datetime.datetime.now().hour, datetime.datetime.now().minute], [datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year], [0, 0]]]
  
  editstate = false
  editdepth = 0
  
  theTime = {}
  theDate = {}
  
  
  
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.bup, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.bup,GPIO.HIGH,self.ButtonHandler)
    GPIO.setup(self.bdown, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.bdown,GPIO.HIGH,self.ButtonHandler)
    GPIO.setup(self.bleft, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.bleft,GPIO.HIGH,self.ButtonHandler)
    GPIO.setup(self.bright, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.bright,GPIO.HIGH,self.ButtonHandler)
    GPIO.setup(self.bset, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.bset,GPIO.HIGH,self.ButtonHandler)
    GPIO.setup(self.bmenu, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.bmenu,GPIO.HIGH,self.ButtonHandler)
    GPIO.setup(self.bsnooze1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.bsnooze1,GPIO.HIGH,self.ButtonHandler)
    GPIO.setup(self.bsnooze2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(self.bsnooze2,GPIO.HIGH,self.ButtonHandler)
  
  def ButtonHandler(channel):
    if channel == self.bup:
      if self.menudepth == 0:
        if mainmenu[0] > 0:
          mainmenu[0] -= 1
      elif self.menudepth == 1:
        if mainmenu[1] > 0:
          mainmenu[1] -= 1
      elif self.menudepth == 2:
        if mainmenu[0] == 1:
          #method for setting alarm
          pass
        if mainmenu[0] == 2:
          #method for setting timer
          pass
        if mainmenu[0] == 3:
          if mainmenu[1] == 0:
            
          if mainmenu[1] == 1:

    if channel == self.bdown:
      pass
    if channel == self.bleft:
      pass
    if channel == self.bright:
      pass
    if channel == self.bset:
      pass
    if channel == self.bmenu:
      pass
    if channel == self.bsnooze1:
      pass
      
  def mainHandler(self, theButton, showDisp):
    pass
    

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
  #theThread = myThread()
  #theThread.start()
  return DisplayOLEDSkill()
