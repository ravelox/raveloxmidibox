import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('config', __name__, url_prefix='/config')

@bp.route('/raveloxmidi', methods=('GET', 'POST'))
def config_raveloxmidi():
	return render_template('config/raveloxmidi.html')

@bp.route('/box', methods=('GET', 'POST'))
def config_box():
	return render_template('config/box.html')

