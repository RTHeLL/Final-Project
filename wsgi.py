import view

from app import app

# Blueprints
from blueprints.pinger.blueprint import pinger
from blueprints.cv_generator.blueprint import cv_generator

app.register_blueprint(pinger, url_prefix='/pinger')
app.register_blueprint(cv_generator, url_prefix='/cv')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
