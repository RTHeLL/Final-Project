from flask import Blueprint, render_template, request, flash

# Import controller
from controller.ping import ping

# Register blueprint
pinger = Blueprint('pinger', __name__, template_folder='templates')


@pinger.route('/', methods=['GET', 'POST'])
def pinger_handler():
    if request.method == 'POST':
        address = request.form['address']
        if ping(address):
            flash(f'Сервер `{address}` доступен!')
            return render_template('pinger_index.html', addr_response=True)
        flash(f'Сервер `{address}` недоступен!')
        return render_template('pinger_index.html', addr_response=False)
    return render_template('pinger_index.html')
