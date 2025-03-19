from flask import redirect, url_for
from . import main

@main.route('/')
def index():
    return redirect(url_for('auth.login'))