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

import os

from flask import Flask

def create_app(test_config=None):
	app = Flask( __name__, instance_relative_config=True )
	app.config.from_mapping(
		SECRET_KEY='dev',
	)

	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	from . import raveloxmidiconfig
	app.register_blueprint(raveloxmidiconfig.bp)
	raveloxmidiconfig.init_app(app)

	from . import buttondisplay
	app.register_blueprint(buttondisplay.bp)
	
	from . import polltest
	app.register_blueprint(polltest.bp)

	@app.route('/whoami')
	def whoami():
		return "Success"

	return app
