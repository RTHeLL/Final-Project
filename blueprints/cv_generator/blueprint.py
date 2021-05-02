import datetime
import json
import os.path
import pathlib

from flask import Blueprint, render_template, request, flash

from app import app, ALLOWED_EXTENSIONS

# Register blueprint
cv_generator = Blueprint('cv_generator', __name__, template_folder='templates')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@cv_generator.route('/', methods=['GET', 'POST'])
def cv_generator_handler():
    date = datetime.datetime.now()
    if request.method == 'POST':
        dict_info = dict(request.form)

        # More info
        names = [i[1] for i in request.form.items() if 'cv_social_name' in i[0]]
        links = [i[1] for i in request.form.items() if 'cv_social_link' in i[0]]
        socials = [{"name": i, "link": v} for i, v in zip(names, links)]

        # Projects
        projects_names = [i[1] for i in request.form.items() if 'cv_project_name' in i[0]]
        projects_links = [i[1] for i in request.form.items() if 'cv_project_link' in i[0]]
        projects_desc = [i[1] for i in request.form.items() if 'cv_project_desc' in i[0]]
        projects = [{"name": i, "link": v, "description": m}
                    for i, v, m in zip(projects_names, projects_links, projects_desc)]

        if request.files['photo'].filename == '':
            flash('Необходимо загрузить фото')
        else:
            photo = request.files['photo']
            if photo and allowed_file(photo.filename):
                pathlib.Path(app.config['UPLOAD_FOLDER'], str(date.date())).mkdir(exist_ok=True)
                path = os.path.join(
                    app.config['UPLOAD_FOLDER'],
                    str(date.date()),
                    str(date.replace(microsecond=0)).replace(' ', '_') + '.' + str(photo.filename.split('.')[-1]))
                photo.save(path)
                dict_info['cv_photo'] = path.replace('static/', '')
                dict_info['cv_social'] = json.dumps(socials)
                dict_info['cv_projects'] = json.dumps(projects)
                flash('Изображение успешно загружено', )
            else:
                flash('Необходимо загружать изображение формата PNG, JPG, JPEG или GIF')

        return render_template('cv_done.html', dict_info=dict_info)

    return render_template('cv_index.html', all_done=True)
