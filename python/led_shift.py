#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings( False )
 
SER_PIN	= 18
LATCH_PIN = 23
CLOCK_PIN = 24
CLEAR_PIN = 25

GPIO.setup(SER_PIN, GPIO.OUT)
GPIO.setup(LATCH_PIN, GPIO.OUT)
GPIO.setup(CLOCK_PIN, GPIO.OUT)
GPIO.setup(CLEAR_PIN, GPIO.OUT)

#
# Initialise the pins
#
def init_pins():
	GPIO.output( CLEAR_PIN, 0 )
	GPIO.output( CLEAR_PIN, 1 )

#
# Toggle the clock pin
#
def tick_clock():
	GPIO.output( CLOCK_PIN, 1 )
	GPIO.output( CLOCK_PIN, 0 )


#
# Set a data bit
#
def clock_data( bit ):
	GPIO.output( SER_PIN, bit )
	tick_clock()


#
# Send a whole byte
#
def shift_byte( byte ):
	x=7
	GPIO.output( LATCH_PIN, 0)
	while x >= 0:
		mask = ( 1 << x )
		data_bit =  byte & mask
		print mask," ",data_bit
		clock_data( data_bit )
		x = x - 1
	GPIO.output( LATCH_PIN, 1)

init_pins()
shift_byte( 92 )
