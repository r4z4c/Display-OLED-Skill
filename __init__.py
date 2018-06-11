
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
  mainmenu[] = {0,{{2, 2, 2}, {2, 2, 2}, {2, 2}}, {},{1}}
  
  editstate = false
  editdepth = 0
  
  theTime = None
  theDate = None
  
  
  
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
    switch(channel) {
      case self.bup:
        if self.editstate:
          
        else:
          if mainmenu[0] == 0:
            if menudepth == 0:
              mainmenu[0] += 1
          if mainmenu[0] == 1:
            if menudepth == 0:
              mainmenu[0] += 1
            elif menudepth == 1:
              if mainmenu[1] == 0:
                mainmenu[1]
            elif menudepth == 2
      
          elif mainmenu[] == 
            
            
        break;
      case self.bdown:
      
        break;
      case self.bleft:
      
        break;
      case self.bright:
      
        break;
      case self.bset:
      
        break;
      case self.bmenu:
      
        break;
      case self.bsnooze1:
    }
      
  def mainHandler(self, theButton, showDisp):
    

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
