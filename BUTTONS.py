
import RPi.GPIO as GPIO
from subprocess import call
import time
from mycroft.messagebus.client.ws import WebsocketClient
from mycroft.messagebus.message import Message


class theButtons:

    myDisplay = None
    myLEDs = None

    messagebusClient = WebsocketClient()

    def __init__(self, theDisplay, theLEDs):
        self.myDisplay = theDisplay
        self.myLEDs = theLEDs

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(17, GPIO.RISING, callback=self.button_shutdown())
        GPIO.add_event_detect(23, GPIO.RISING, callback=self.button_stop_alarm())
        GPIO.add_event_detect(24, GPIO.RISING, callback=self.button_stop_alarm())

    def onConnected(self, event=None):
        self.messagebusClient.emit(Message("recognizer_loop:utterance",data={'utterances': 'cancel alarm'}))
        self.messagebusClient.close()

    def button_shutdown(self, channel):
        self.myDisplay.config['show'] = 'off'
        self.myLEDs.config['show'] = 'off'
        time.sleep(1)
        call(['sudo shutdown now'])

    def button_stop_alarm(self, channel):
        if GPIO.input(23) and GPIO.input(24):
            self.messagebusClient.on('connected', self.onConnected)
            # This will block until the client gets closed
            self.messagebusClient.run_forever()
