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

import socket
import struct
import time

class raveloxmidi(object):

	def __init__(self, host="localhost", port=5006):
		self.__socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
		self.host = host
		self.port = port
		self.__state = 1

	def connect(self):
		self.__socket.connect( (self.host, self.port) )

	def close(self):
		self.__socket.close()

	def send_note(self, channel, note, velocity):
		if channel > 15:
			channel = channel & 0x0f

		try:
# Note ON
			command = 0x90 | channel
			bytes = struct.pack( "BBBB", 0xaa,command, note, velocity )
			self.__socket.send( bytes )

			time.sleep( 0.25 )
# Note OFF
			command = 0x80 | channel
			bytes = struct.pack( "BBBB", 0xaa, command, note, velocity )
			self.__socket.send( bytes )
		except:
			print "Something went wrong"
