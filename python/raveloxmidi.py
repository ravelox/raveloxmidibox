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

	__host = None
	__port = 0

	def __init__(self, host="localhost", port=5006):
		self.__socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
		self.__host = host
		self.__port = port
		self.__state = 1

	def connect(self):
		self.__socket.connect( (self.__host, self.__port) )

	def close(self):
		self.__socket.close()

# Note ON
	def note_on(self, channel, note, velocity):
		if channel > 15:
			channel = channel & 0x0f
		command = 0x90 | channel
		bytes = struct.pack( "BBB", command, note, velocity )
		try:
			self.__socket.send( bytes )
		except:
			print "Unable to send NoteOn"

# Note OFF
	def note_off(self, channel, note, velocity):
		if channel > 15:
			channel = channel &0x0f
		command = 0x80 | channel
		bytes = struct.pack( "BBB", command, note, velocity )
		try:
			self.__socket.send( bytes )
		except:
			print "Unable to send NoteOff"
