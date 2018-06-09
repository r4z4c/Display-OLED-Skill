#!/usr/bin/python
# coding=utf-8

# this is my script for my alarm to handle the oled display

import sys, os, time, json

import DISPLAY as d

display = d.create()

try:
  while True:
    pass

finally:
  GPIO.cleanup()
  display.reset()
