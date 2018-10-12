import json
import functools
import os

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import current_app as app

import click
from flask.cli import with_appcontext

bp = Blueprint('buttondisplay', __name__, url_prefix='/buttondisplay')

@bp.route('/', methods=('GET', 'POST'))
def config_box():
	return render_template('buttondisplay/buttons.html')
