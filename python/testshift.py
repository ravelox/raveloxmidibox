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
import time

l = ledshift()
b = buttonshift()

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

while True:
	(button_value, button_count) = b.poll_buttons()
	l.shift_byte( button_value )
