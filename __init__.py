
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

menudepth = 0
mainmenu = [0, 0, 0]
submenu = [0, 0, 0, 0, 0]

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
    switch(channel) {
      case self.bup:
        if not self.editstate:
          if mainmenu[0] == 1: #Alarm
            if menudepth == 0:
              mainmenu[0] -= 1 #to Time/Date
            elif menudepth == 1:
      
          elif mainmenu[0] == 2: #Timer
            if menudepth == 0:
              mainmenu[0] -= 1 #to Alarm
            elif menudepth == 1:
      
          elif mainmenu[0] == 2: #Music
            if menudepth == 0:
              mainmenu[0] -= 1 #to Timer
            elif menudepth == 1:
      
          elif mainmenu[0] == 3: #Config
            if menudepth == 0: 
              mainmenu[0] -= 1 #to Music
            elif menudepth == 1: 
              if mainmenu[1] == 1:
                mainmenu[1] -= 1 #to Time
              elif mainmenu[1] == 2:
                mainmenu[1] -= 1 #to Date

          
          
          elif mainmenu[0] == 3: #Alarm
            if menudepth == 0:
              mainmenu[0] -= 1 #to Time/Date
        else:
          if menudepth == 2:
              if mainmenu[1] == 0: #Time
                if mainmenu[2] == 0: #Hour
                  if self.theTime[0] < 12:
                    self.theTime[0] += 1
                  else:
                    theTime[0] = 1
      
                elif mainmenu[2] == 1: #Minute
                  
      
                elif mainmenu[2] == 2: #Second
                  
      
              elif mainmenu[1] == 1: #Date
      
              elif mainmenu[1] == 2: #Out/In
            
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
