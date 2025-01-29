FROM registry.dulno.com/dulno-obfuscation:latest AS builder

RUN mkdir -p /home/dulno/web
RUN ln -s /obfuscation /home/dulno/web

COPY web/static /home/dulno/web/static
COPY web/obfuscation /home/dulno/web/obfuscation

ENV OBFUSCATION_HOME=/home/dulno/web

RUN node /home/dulno/web/obfuscation/obfuscate.js

FROM alpine
COPY --from=builder /home/dulno/web/static /static/