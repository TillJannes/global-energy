FROM alpine:latest

RUN mkdir /scripts \
    && apk --update add postgresql-client
COPY ./0001_setup.sql /scripts

WORKDIR /
CMD ["/bin/sh", "-c", "/usr/bin/psql postgresql://${ENERGY_USER}:${ENERGY_PASSWORD}@energy-db:${ENERGY_PORT}/${ENERGY_DB} -f /scripts/0001_setup.sql"]
