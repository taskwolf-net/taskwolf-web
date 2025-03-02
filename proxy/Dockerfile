ARG DOCKER_REGISTRY
FROM ${DOCKER_REGISTRY}/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/web
RUN ln -s /obfuscation /home/dulno/web

COPY static /home/dulno/web/static
COPY obfuscation /home/dulno/web/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/web

RUN node /home/dulno/web/obfuscation/obfuscate.js

FROM nginx

ARG SERVER_NAME
ENV SERVER_NAME=${SERVER_NAME}

COPY --from=builder /home/dulno/web/static /home/dulno/web/static/

COPY proxy/nginx.conf /etc/nginx/nginx.conf
COPY proxy/proxy /etc/nginx/sites-available/proxy
RUN ln -sf /etc/nginx/sites-available/proxy /etc/nginx/sites-enabled/proxy

CMD ["/bin/sh", "-c", "envsubst '$SERVER_NAME' < /etc/nginx/sites-available/proxy > /tmp/proxy && mv /tmp/proxy /etc/nginx/sites-available/proxy && exec nginx -g 'daemon off;'"]