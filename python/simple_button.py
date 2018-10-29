#!/usr/bin/python
import RPi.GPIO as GPIO
import time

num_buttons = 8;
buttonPin = 17
serialPin = 3
latchPin = 4
clockPin = 27
clearPin = 22

#
# Use Broadcom GPIO pin numbering
#
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#
# Set up the GPIO pins
#
GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(serialPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT)
GPIO.setup(clockPin, GPIO.OUT)
GPIO.setup(clearPin, GPIO.OUT)

#
# Reset the shift register
#
GPIO.output( latchPin, 0 )
GPIO.output( clearPin, 0 )
GPIO.output( clearPin, 1 )
GPIO.output( latchPin, 1 )

countdown = 5
while countdown > 0:
        print( countdown )
        time.sleep(1)
        countdown = countdown - 1
print("\n")

x = 0
button_presses = 0
#
# Set the serial pin high for the first button
#
GPIO.output( serialPin, 1 )

#
# Check each button
#
while x < num_buttons:
    #
    # Clock the data
    #
    GPIO.output( latchPin, 0 )
    GPIO.output( clockPin, 1 )
    GPIO.output( clockPin, 0 )
    GPIO.output( latchPin, 1 )

    #
    # Read the input pin to see if the current button has been pressed
    #
    result = GPIO.input( buttonPin ) 
    if result == GPIO.HIGH:
        button_presses = button_presses + ( 1 << x )
    x = x + 1
    GPIO.output( serialPin, 0 )

print  "Button value = ",button_presses
