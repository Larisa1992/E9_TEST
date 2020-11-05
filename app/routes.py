from app import app, db

from datetime import datetime, timedelta

from flask import jsonify, render_template, request, redirect, flash
from app.models import Event
from app.forms import EventsForm

@app.route('/')
@app.route('/hello')
def index():
    return f"Hi, fellow Flask developer!"