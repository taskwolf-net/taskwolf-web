FROM python:3

RUN pip install django
RUN pip install gunicorn
RUN pip install django-cors-headers
RUN pip install requests
RUN pip install jwt

COPY . .

ENTRYPOINT ["gunicorn","--config","app/gunicorn-config.py", "app.wsgi"]