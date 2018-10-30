#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import sys
 
num_leds = 8
serialPin = 18
latchPin = 23
clockPin = 24
clearPin = 25

#
# Use the Broadcom numbering for GPIO pins
#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings( False )
 
#
# Set up the GPIO pins
#
GPIO.setup(serialPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT)
GPIO.setup(clockPin, GPIO.OUT)
GPIO.setup(clearPin, GPIO.OUT)

#
# Clear the shift register
# 
GPIO.output( latchPin, 0 )
GPIO.output( clearPin, 0 )
GPIO.output( clearPin, 1 )
GPIO.output( latchPin, 1 )

byte = int( sys.argv[1] )
x = num_leds - 1

GPIO.output( latchPin, 0)
while x >= 0:
	mask = ( 1 << x )
	data_bit =  byte & mask
	GPIO.output( serialPin, data_bit )
	GPIO.output( clockPin, 1 )
	GPIO.output( clockPin, 0 )
	x = x - 1
GPIO.output( latchPin, 1)
