import view

from app import app

# Blueprints
from blueprints.pinger.blueprint import pinger

app.register_blueprint(pinger, url_prefix='/pinger')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
