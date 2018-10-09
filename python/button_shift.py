#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
BUTTON_PIN = 26
SER_PIN	= 3
LATCH_PIN = 4
CLOCK_PIN = 27 
CLEAR_PIN = 22

GPIO.setup(BUTTON_PIN, GPIO.IN)

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
# Poll the buttons by making each pin high
# and testing the button pin
#
def poll_buttons():
	button_presses = 0
	x = 0
	while x < 8:
		GPIO.output( LATCH_PIN, 0 )
		tick_clock()
		GPIO.output( LATCH_PIN, 1 )
		result = GPIO.input( BUTTON_PIN ) 
		if result == GPIO.HIGH:
			button_presses = button_presses + ( 1 << x )
		x = x + 1
		GPIO.output( SER_PIN, 0 )
	return button_presses

init_pins()

prev_result = 0
while True:
	GPIO.output( SER_PIN, 1 )
	this_result = poll_buttons()
	if this_result <> prev_result:
		print this_result
		prev_result = this_result
