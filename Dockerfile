ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN ln -s /obfuscation /web

COPY . /web

WORKDIR /web

ENV OBFUSCATION_HOME=/web

RUN node obfuscation/obfuscate.js

FROM python:3.13-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends gettext linux-libc-dev curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir django gunicorn django-cors-headers requests jwt

COPY --from=builder /web /web

WORKDIR /web

RUN django-admin compilemessages

ENTRYPOINT ["gunicorn", "--config", "app/gunicorn-config.py", "app.wsgi"]