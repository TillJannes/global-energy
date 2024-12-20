FROM alpine:latest

RUN mkdir /scripts \
    && apk --update add postgresql-client
COPY ./0001_setup.sql /scripts

WORKDIR /
CMD ["/bin/sh", "-c", "/usr/bin/psql postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB} -f /scripts/0001_setup.sql"]
