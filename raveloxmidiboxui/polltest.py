import json
import functools
import os
import datetime

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app

import click
from flask.cli import with_appcontext

bp = Blueprint('polltest', __name__, url_prefix='/polltest')

@bp.route('/', methods=('GET', 'POST'))
def config_box():
	return render_template('polltest/polltest.html')

@bp.route('/polldate', methods=('GET', 'POST'))
def get_date():
	return "{ \"returnstring\":\"" + datetime.datetime.now().isoformat() + "\"}"
