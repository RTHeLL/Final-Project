FROM python:3.8.5

RUN useradd --create-home kinderfinalproject
WORKDIR /Final-Project

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        apt-utils \
        build-essential \
        curl \
        git \
        libbz2-dev \
        libncurses5-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        llvm \
        make \
        tk-dev \
        wget \
        xz-utils \
        zlib1g-dev \
        locales locales-all \
    && pip install pipenv

RUN /bin/bash -c "/usr/local/bin/python3.8 -m pip install --upgrade pip"

COPY ./ .
RUN pipenv install --system --deploy

RUN chown -R kinderfinalproject:kinderfinalproject ./
USER kinderfinalproject

EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:8000 wsgi:app --timeout 200
