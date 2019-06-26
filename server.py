from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

import data_manager

app = Flask(__name__)

@app.route('/')
def index():
    recent_sessions = data_manager.get_recent_sessions()
    return render_template('index.html', recent_sessions=recent_sessions)
