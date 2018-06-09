#!/usr/bin/python

# this is my script for my alarm to handle the oled display

import RPi.GPIO as GPIO
import sys, os, time, json

import DISPLAY

newdisplay = ShowOnDisplay()

try:
  while True:
    pass
  
finally:
  GPIO.cleanup()
