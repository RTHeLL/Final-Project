import locale

from datetime import datetime

from app import app
from flask import render_template

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')


@app.route('/')
def index_handler():
    date = datetime.now().date()
    return render_template('index.html', date=date.strftime('%d %B %Y'))
