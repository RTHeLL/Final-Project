FROM python:3.8.5

RUN useradd --create-home kinderfinalproject
WORKDIR /Final-Project

RUN apt-get update \
    && apt-get install -y locales locales-all \
    && apt-get install -y --no-install-recommends gcc \
    && pip install pipenv

RUN /bin/bash -c "/usr/local/bin/python3.8 -m pip install --upgrade pip"

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
RUN pipenv run pip freeze

COPY ./ .

RUN chown -R kinderfinalproject:kinderfinalproject ./
USER kinderfinalproject

EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:8000 wsgi:app
