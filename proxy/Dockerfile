ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/web
RUN ln -s /obfuscation /home/dulno/web

COPY static /home/dulno/web/static
COPY obfuscation /home/dulno/web/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/web

RUN node /home/dulno/web/obfuscation/obfuscate.js

FROM nginx

COPY --from=builder /home/dulno/web/static /home/dulno/web/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
COPY proxy/proxy /etc/nginx/sites-enabled/proxy

RUN rm /etc/nginx/conf.d/default.conf