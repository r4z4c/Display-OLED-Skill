
import RPi.GPIO as GPIO
from subprocess import call
import time
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message


class theButtons:

    myDisplay = None
    myLEDs = None

    messagebusClient = WebsocketClient()

    pin1 = 17
    pin2 = 27
    pin3 = 22

    def __init__(self, theDisplay, theLEDs):
        self.myDisplay = theDisplay
        self.myLEDs = theLEDs

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.pin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.pin1, GPIO.RISING, self.button_shutdown())
        GPIO.add_event_detect(self.pin2, GPIO.RISING, self.button_stop_alarm())
        GPIO.add_event_detect(self.pin3, GPIO.RISING, self.button_stop_alarm())

    def onConnected(self, event=None):
        self.messagebusClient.emit(Message("recognizer_loop:utterance",data={'utterances': 'cancel alarm'}))
        self.messagebusClient.close()

    def button_shutdown(channel, self):
        self.myDisplay.config['show'] = 'off'
        self.myLEDs.config['show'] = 'off'
        time.sleep(1)
        call(['sudo shutdown now'])

    def button_stop_alarm(channel, self):
        if GPIO.input(self.pin2) and GPIO.input(self.pin3):
            self.messagebusClient.on('connected', self.onConnected)
            # This will block until the client gets closed
            self.messagebusClient.run_forever()
