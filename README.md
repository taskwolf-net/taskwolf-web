<div align="center">
  <img src="https://dulno.com/static/img/logo-light.webp" alt="logo" width="128"  height="auto" />

  <h1><b>Dulno - Web</b><br><br></h1>

</div>

The entire web application is managed in this repository. The project can be divided into two sections. The frontend offers the users a pleasant interface to work with Dulno. And the backend communicates with the system to run the processes as efficiently as possible.

## Status

|      | Pipeline status                                                     |
|------|---------------------------------------------------------------------|
| main | ![](https://git.dulno.com/dulno/dulno-web/badges/main/pipeline.svg) |
| dev  | ![](https://git.dulno.com/dulno/dulno-web/badges/dev/pipeline.svg)  |

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