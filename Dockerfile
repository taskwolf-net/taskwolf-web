FROM registry.dulno.com/dulno-obfuscation:latest AS builder

RUN ln -s /obfuscation /web

COPY . /web

WORKDIR /web

ENV OBFUSCATION_HOME=/web

RUN node obfuscation/obfuscate.js

FROM python:3

RUN pip install django
RUN pip install gunicorn
RUN pip install django-cors-headers
RUN pip install requests
RUN pip install jwt

COPY --from=builder /web /web

WORKDIR /web

ENTRYPOINT ["gunicorn","--config","app/gunicorn-config.py", "app.wsgi"]