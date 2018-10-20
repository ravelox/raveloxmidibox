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
 
class ledshift(object):

	def __init__(self, numLEDs=8, serialPin=18, latchPin=23, clockPin=24, clearPin=25):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings( False )
 
		self.SER_PIN	= serialPin 
		self.LATCH_PIN = latchPin
		self.CLOCK_PIN = clockPin
		self.CLEAR_PIN = clearPin 
		self.__num_leds= numLEDs

		GPIO.setup(self.SER_PIN, GPIO.OUT)
		GPIO.setup(self.LATCH_PIN, GPIO.OUT)
		GPIO.setup(self.CLOCK_PIN, GPIO.OUT)
		GPIO.setup(self.CLEAR_PIN, GPIO.OUT)
		self.reset()

	def reset(self):
		GPIO.output( self.LATCH_PIN, 0 )
		GPIO.output( self.CLEAR_PIN, 0 )
		GPIO.output( self.CLEAR_PIN, 1 )
		GPIO.output( self.LATCH_PIN, 1 )

#
# Toggle the clock pin
#
	def __tick_clock(self):
		GPIO.output( self.CLOCK_PIN, 1 )
		GPIO.output( self.CLOCK_PIN, 0 )


#
# Set a data bit
#
	def __clock_data( self, bit ):
		GPIO.output( self.SER_PIN, bit )
		self.__tick_clock()

#
# Send a whole byte
#
	def shift_byte( self, byte ):
		x=( self.__num_leds - 1 )
		GPIO.output( self.LATCH_PIN, 0)
		while x >= 0:
			mask = ( 1 << x )
			data_bit =  byte & mask
			self.__clock_data( data_bit )
			x = x - 1
		GPIO.output( self.LATCH_PIN, 1)

	def selftest( self ):
		test_pattern = [ 34, 89, 123, 22, 1, 5, 73, 61, 99, 108 ]
		for p in test_pattern:
			print "Test: ",p
			self.shift_byte( p )
			time.sleep( 2 )
