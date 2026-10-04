# Dulno - Web

[![CI](https://github.com/taskwolf-net/taskwolf-web/actions/workflows/ci.yml/badge.svg)](https://github.com/taskwolf-net/taskwolf-web/actions/workflows/ci.yml)

The entire web application is managed in this repository. The project can be divided into two sections. The frontend offers the users a pleasant interface to work with Dulno. And the backend communicates with the system to run the processes as efficiently as possible.

## Installation

```bash
python -m venv env

source env/bin/activate

pip install django gunicorn django-cors-headers requests jwt

django-admin compilemessages

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Run

```bash
source env/bin/activate

gunicorn --config app/gunicorn-config.py app.wsgi
```

## Compile locales

```bash
django-admin compilemessages
```