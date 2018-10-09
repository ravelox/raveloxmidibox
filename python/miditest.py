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

l = ledshift()
b = buttonshift()
r = raveloxmidi()

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

while True:
	buttons = b.poll_buttons()
	l.shift_byte( buttons )

	if isOn( 0x01, prev_state, buttons ):
		r.note_on( 0x06, 0x24, 0x7f )

	if isOff( 0x01, prev_state, buttons ):
		r.note_off( 0x06, 0x24, 0x7f )

	if isOn( 0x02, prev_state, buttons ):
		r.note_on( 0x06, 0x26, 0x7f )

	if isOff( 0x02, prev_state, buttons ):
		r.note_off( 0x06, 0x26, 0x7f )

	prev_state = buttons

r.close()
