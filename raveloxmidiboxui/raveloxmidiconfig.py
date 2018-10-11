import json
import functools
import os

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app

import click
from flask.cli import with_appcontext

bp = Blueprint('config', __name__, url_prefix='/config')

@bp.route('/raveloxmidi', methods=('GET', 'POST'))
def config_raveloxmidi():
	return render_template('config/raveloxmidi.html')

@bp.route('/box', methods=('GET', 'POST'))
def config_box():
	return render_template('config/box.html')

def init_config():
	default_json = json.loads( '{ "buttons" : [ { "button_id":1, "name":"Kick", "type":"note", "midi_channel":6, "midi_id":36, "midi_value":127}, { "button_id":2, "name":"Snare", "type":"note", "midi_channel":6, "midi_id":38, "midi_value":127 }, { "button_id":4, "name":"Tom", "type":"note", "midi_channel":6, "midi_id":40, "midi_value":127 } ], "remote_host" : "localhost", "remote_port" : 5006 }' )

	config_file_name = os.path.join(app.instance_path,"raveloxmidibox.conf")
	with open( config_file_name, 'w') as outputfile:
		json.dump( default_json, outputfile, indent=4)

@click.command('init-config')
@with_appcontext
def init_config_command():
	init_config()
	click.echo('Config initialized')

def init_app(app):
	app.cli.add_command(init_config_command)
