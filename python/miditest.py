#!/usr/bin/python

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

from buttonshift import *
from ledshift import *
from raveloxmidi import *
from config import *

import pprint

l = ledshift()
b = buttonshift()
c = config("config.json")

cb = c['buttons']

r = raveloxmidi( c['remote_host'], c['remote_port'] )
r.connect()

prev_state = 0

def isOn( button, oldstate, newstate):
	button_prev = oldstate & button
	button_now = newstate & button
	return_val = False
	if button_prev==0 and button_now>0:
		return_val = True
	return return_val

def isOff( button, oldstate, newstate ):
	button_prev = oldstate & button
	button_now = newstate & button
	return_val = False
	if button_prev>0 and button_now==0:
		return_val = True
	return return_val

if c['num_buttons'] == 0:
	x = 5
	print "Press the last button and hold it"
	while x > 0:
		time.sleep(1)
		print(x)
		x = x - 1
	time.sleep(1)

	print "Checking buttons"
	available_buttons = b.discover()
	print str(available_buttons) + " buttons found"
	print "Let go of the button and wait"
	time.sleep(5)
else:
	b.set_num_buttons( c['num_buttons'] )

print "OK"

while True:
	(button_value, button_count) = b.poll_buttons()
	l.shift_byte( button_value )

	for button in cb:
		if isOn( button['button_id'], prev_state, button_count ):
			r.note_on( button['midi_channel'], button['midi_id'], button['midi_value'] )
			print button['name']

		if isOff( button['button_id'], prev_state, button_count ):
			r.note_off( button['midi_channel'], button['midi_id'], button['midi_value'] )

	prev_state = button_count

r.close()
