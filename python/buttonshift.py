#    This file is part of raveloxmidibox.
#
#    raveloxmidibox is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    raveloxmidibox is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with raveloxmidibox.  If not, see <https://www.gnu.org/licenses/>.

import RPi.GPIO as GPIO
import time
import math

class buttonshift(object):
	__num_buttons = 8;
	def __init__(self, buttonPin=17, serialPin=3, latchPin=4, clockPin=27, clearPin=22):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		self.BUTTON_PIN = buttonPin
		self.SER_PIN	= serialPin
		self.LATCH_PIN = latchPin
		self.CLOCK_PIN = clockPin
		self.CLEAR_PIN = clearPin
		self.reset()

	def reset(self):
		GPIO.setup(self.BUTTON_PIN, GPIO.IN)
		GPIO.setup(self.SER_PIN, GPIO.OUT)
		GPIO.setup(self.LATCH_PIN, GPIO.OUT)
		GPIO.setup(self.CLOCK_PIN, GPIO.OUT)
		GPIO.setup(self.CLEAR_PIN, GPIO.OUT)
#
# Initialise the pins
#
		self.__toggle_clear()

#
# Toggle the clock pin
#
	def __tick_clock(self):
		GPIO.output( self.CLOCK_PIN, 1 )
		GPIO.output( self.CLOCK_PIN, 0 )
#
# Toggle the clear pin
#
	def __toggle_clear(self):
		GPIO.output( self.CLEAR_PIN, 0 )
		GPIO.output( self.CLEAR_PIN, 1 )

	def set_num_buttons(self, numButtons):
		self.__num_buttons = numButtons

#
# Poll the buttons by making each pin high
# and testing the button pin
#
	def poll_buttons(self):
		button_presses = 0
		x = 0
		m = 0
		self.__toggle_clear()
		GPIO.output( self.SER_PIN, 1 )
		while x < self.__num_buttons:
			GPIO.output( self.LATCH_PIN, 0 )
			self.__tick_clock()
			GPIO.output( self.LATCH_PIN, 1 )
			result = GPIO.input( self.BUTTON_PIN ) 
			if result == GPIO.HIGH:
				button_presses = button_presses + ( 1 << x )
				m = max( m, x+1 )
			x = x + 1
			GPIO.output( self.SER_PIN, 0 )
		return button_presses, m

	def discover(self):
		old_buttons = self.__num_buttons;
		self.__num_buttons = 256;
		(button_value,button_max) = self.poll_buttons()
		if button_value == 0:
			self.__num_buttons = old_buttons
		else:
			self.__num_buttons = button_max
		return self.__num_buttons

	def selftest(self):
		prev_result = 0
		while True:
			(this_result,button_max) = self.poll_buttons()
			if this_result != prev_result:
				print("Button value ",this_result," Max=",button_max)
				prev_result = this_result
