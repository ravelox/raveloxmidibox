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

import json

class config(object):
	__filename = None
	__json_data= None
	__state = 0
	def __init__(self, filename):
		if not self.__filename:
			self.__filename = filename
		self.__state = 0

	def __load(self):
		if not self.__filename:
			return
		self.__json_data = json.loads( open( self.__filename).read() )
		self.__state = 1

	def __getitem__(self, str):
		if not self.__filename:
			return None
		if self.__state <> 1:
			self.__load()
		return self.__json_data[ str ]
