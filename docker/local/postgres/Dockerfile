FROM postgres:14.1

COPY ./docker/local/postgres/maintainance /usr/local/bin/maintainance

RUN chmod +x /usr/local/bin/maintainance/*
RUN mv /usr/local/bin/maintainance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintainance

